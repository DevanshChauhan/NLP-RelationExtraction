import json
import sys

import typer

from pathlib import Path

from spacy.tokens import Span, DocBin, Doc
from spacy.vocab import Vocab
from wasabi import Printer
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
from spacy.util import compile_infix_regex, filter_spans
import re
import spacy

# Create a Tokenizer using scibert
nlp = spacy.load("en_core_sci_scibert")


msg = Printer()

MAP_LABELS = {
    "Positive_Correlation": "Positive_Correlation",
    "Negative_Correlation": "Negative_Correlation",
    "Association": "Association",
    "Bind": "Bind",
    "Cause": "Cause",
    "Cotreatment": "Cotreatment",
    "Drug_Interaction": "Drug_Interaction",
    "Comparison": "Comparison"
}


train_ifile = "assets/Train.BioC.json"
dev_ifile = "assets/Dev.BioC.json"
test_ifile = "assets/Test.BioC.json"
train_ofile='data/Train_BioC.spacy'
dev_ofile='data/Dev_BioC.spacy'
test_ofile='data/Test_BioC.spacy'

def main(json_loc: Path, json_loc1: Path, json_loc2: Path, train_file: Path, dev_file: Path, test_file: Path):
    
    filepaths = [(json_loc,train_file), (json_loc1,dev_file), (json_loc2,test_file)]

    for inpfil, outfil in filepaths:
        """Creating the corpus from the JSON annotations."""
        Doc.set_extension("rel", default={},force=True)
        vocab = Vocab()

        docs = {"train": [], "dev": [], "test": [], "total": []}
        ids = {"train": set(), "dev": set(), "test": set(), "total":set()}
        count_all = {"train": 0, "dev": 0, "test": 0,"total": 0}
        count_pos = {"train": 0, "dev": 0, "test": 0,"total": 0}

        with open(inpfil, encoding="utf8") as jsonfile:
            file = json.load(jsonfile)
            for passages in file["documents"]:
                
                    
                span_starts = set()
                neg = 0
                pos = 0
                pass1 = ""
                
                for example in passages["passages"]:
                    if pass1 != "":
                        pass1 = pass1 + " " + example["text"]
                    else:
                        pass1 = example["text"]     
                
                # Parse the tokens
                tokens=nlp(pass1)    
                spaces=[]
                spaces = [True if tok.whitespace_ else False for tok in tokens]
                words = [t.text for t in tokens]
                doc = Doc(nlp.vocab, words=words, spaces=spaces)


                # Parse the GGP entities
                entities = []
                span_end_to_start = {}
                start_list = []
                identifiers = []
                for example in passages["passages"]:
                    spans = example["annotations"]
                    
                    for span in spans:
                        start = span["locations"][0]["offset"]
                        end = start + span["locations"][0]["length"]
                        entity = doc.char_span(
                            start, end, label=span["infons"]["type"] , alignment_mode = 'expand' 
                        )

                        
                        token_start = entity.start
                        
                        if "," in span["infons"]["identifier"]:
                            id =  span["infons"]["identifier"].split(',')
                            span["infons"]["identifier"] = id[0]
                            identifier = {id[i] : id[0] for i in range(1,len(id))}
                            identifiers.append(identifier)
                    
                        if ( token_start not in start_list and entity not in entities ) or span["infons"]["identifier"] in ['C537689','1066','20850','D018698','686326', 'D012871', 'D005947','1457'] :
                            start_list.append(start)
                            span_end_to_start[token_start] = span["infons"]["identifier"] 
                            start_list.append(token_start)
                            entities.append(entity)
                            span_starts.add(token_start)

                filt_entities = filter_spans(entities)
                doc.ents = filt_entities

                # Parse the relations
                rels = {}
                for x1 in span_starts:
                    for x2 in span_starts:
                        rels[(x1, x2)] = {}

                relations = passages["relations"]
                for relation in relations:
                # the 'head' and 'child' annotations refer to the end token in the span
                # but we want the first token
                    for identifier in identifiers:
                        if relation["infons"]["entity1"] in identifier.keys():
                            relation["infons"]["entity1"] = identifier[relation["infons"]["entity1"]]
                        elif relation["infons"]["entity2"] in identifier.keys():
                            relation["infons"]["entity2"] = identifier[relation["infons"]["entity2"]]

                    try:
                        start = list(span_end_to_start.keys())[list(span_end_to_start.values()).index(relation["infons"]["entity1"])]
                        end = list(span_end_to_start.keys())[list(span_end_to_start.values()).index(relation["infons"]["entity2"])]
                    except ValueError:
                        continue
                    else:
                        label = relation["infons"]["type"]
                        
                        if label not in rels[(start, end)]:
                            rels[(start, end)][label] = 1.0
                            pos += 1
                            
                # The annotation is complete, so fill in zero's where the data is missing
                for x1 in span_starts:
                    for x2 in span_starts:
                        for label in MAP_LABELS.values():
                            if label not in rels[(x1, x2)]:
                                neg += 1
                                rels[(x1, x2)][label] = 0.0

                                #print(rels[(x1, x2)])
                doc._.rel = rels

                # only keeping documents with at least 1 positive case
                if pos > 0:
                        docs["total"].append(doc)
                        count_pos["total"] += pos
                        count_all["total"] += pos + neg

                            
                        
        docbin = DocBin(docs=docs["total"], store_user_data=True)
        docbin.to_disk(outfil)
        print(len(docs['total']))
        msg.info(
            f"{len(docs['total'])} training sentences"
        )


main(train_ifile, dev_ifile, test_ifile, train_ofile, dev_ofile, test_ofile)