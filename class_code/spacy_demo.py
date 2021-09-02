#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 16:58:46 2021

@author: dieter
"""

import spacy
from spacy import displacy
import urllib

text = """
Researchers at the University of Cincinnati identified a new species of mosasaur — an 18-foot-long fish-eating monster that lived 80 million years ago.

UC assistant professor-educator Takuya Konishi and his student, UC graduate Alexander Willman, named the mosasaur Ectenosaurus everhartorum after paleontologists Mike and Pamela Everhart. The mosasaur inhabited the Western Interior Seaway in what today is western Kansas.

The discovery was announced Thursday in the Canadian Journal of Earth Sciences.

The newly identified mosasaur marks only the second species in the genus Ectenosaurus.

“Mosasaurs in western Kansas have been well sampled and well researched. Those two factors create tall odds when you try to find something new,” Konishi said.
A false gharial.

The newly named mosasaur, Ectenosaurus everhartorum, resembled a fish-eating crocodile called a false gharial, pictured above. Photo/Wichit Kong/Wikimedia Commons

Mosasaurs were enormous marine reptiles. Some like the one pictured in the top photo were as big as school buses. They inhabited oceans around the world during the Cretaceous period around the time of Tyrannosaurus rex. If Ectenosaurus clidastoides with its long, slender jaws resembles a gharial crocodile, Konishi said the new species is closer to a false gharial crocodile with notably blunter jaws.

Konishi, who teaches in the Biological Sciences Department of UC's College of Arts and Sciences, first encountered the fossil in 2004 while working as a graduate student in systematics and evolution. Konishi was studying fossils of Platecarpus, a different genus of mosasaur in storage at Fort Hays State University's Sternberg Museum of Natural History, when he recognized something odd about one specimen.

“It wasn’t a platecarpus. The frontal bone above the eye socket was much longer. The bones of Platecarpus should have had a broader triangle,” he said. “That was one telltale sign.”
Drawings of a mosasaur jawbone are superimposed next to photos of the fossils and of a similar species.

UC graduate Alexander Willman made scientific drawings of the mosasaur fossils to help understand its taxonomy and to compare it with the jawbone of a similar species, Ectenosaurus clidastoides, labeled D.

Konishi suspected the specimen was a type of ectenosaur, only one species of which had been identified. But the teeth seemed all wrong. The now-empty sockets that would have contained the mosasaur’s sharp, curved teeth in the unidentified specimen would have extended around the front of its mouth, unlike other recognized species that has a toothless rostrum, the bony protuberance at the front of the mouth.

For years, the fossils puzzled him.

“Some things just stick in your mind and they’re hard to let go,” he said.

But the mystery would have to wait because Konishi was busy finishing his doctoral degree and launching an academic career that would bring him to UC’s College of Arts and Sciences.
A scenic vista of exposed limestone hills.

The Smoky Hill Chalk Member of Kansas is a fossil-rich area in western Kansas. Photo/Takuya Konishi

The first mosasaur fossils were found in the Netherlands a half-century before anyone used the term “dinosaur.” Mosasaurs began to capture the nation’s attention after the Civil War when the nation’s premier paleontologists, Othniel Charles Marsh and Edward Drinker Cope, began to study Cretaceous limestone known as the Kansas Chalk in a partnership that became a bitter public feud. Since then, Kansas has become world-renowned for mosasaur research.

Generations of experts have come to Kansas to study its specimens, which are on display at museums around the world.

“It’s a famous place for mosasaur research. It’s quite well known,” Konishi said. “So I thought I don’t have to be the guy to place a stake. I’m sure someone will catch it. But nobody did.”

Ectenosaur is unusual for how few specimens have been found in the genus compared to other mosasaurs, Konishi said.

“In western Kansas we have over 1,500 mosasaur specimens. Out of those we can only find one specimen each representing these two species of ectenosaur,” Konishi said. “That’s sort of crazy.”
Alexander Willman sits at a laptop.

UC graduate Alexander Willman contributed to the research project. Photo/Takuya Konishi

When Konishi confirmed with the Sternberg Museum that no other researchers were studying the specimen, he asked them to ship the fossils to UC. When he opened the carefully bubble-wrapped contents, his initial impressions were confirmed.

“By then I had looked at all the other known Platecarpus specimens under the sun, as it were. And this specimen was distinct from the others,” he said. “To me it was so obvious.”

At the same time, Konishi’s student Willman inquired about working on a research project. He received a UC Undergraduate STEM Experience grant to help with the taxonomic identification.

“I was beyond excited to be part of the discovery,” Willman said.

The third author on the study, Michael Caldwell, is a professor of biology at the University of Alberta, Edmonton.
Ectenosaurus clidastoides

UC researchers identified the mosasaur as belonging to the same genus as Ectenosaurus clidastoides, pictured. The above specimen was found in Kansas in 1953. Photo/Mike Everhart

Willman illustrated the fossils in painstaking detail to help scientists understand the morphological differences that make the mosasaur unique.

“I was very happy with how he brought these broken bones to life,” Konishi said. “It helped make our case very convincing to anyone that this is something new that warrants the establishment of a new taxon.”

Many undergraduate students at UC have a chance to work on original research. Willman said he is happy he took advantage of the opportunity.

“It was a great experience. For those interested in research at UC, I say you just have to put yourself out there and see what you can get involved in,” Willman said. “You never know what might come of it!”
Two students kneel at an excavation site with brushes and tools.

UC assistant professor-educator Takuya Konishi, left, conducts fieldwork in Kansas' fossil-rich Smoky Hill Chalk as a graduate student with researcher Takehito Ikejiri in this 2004 photo. Photo/Mike Everhart

The researchers dedicated the project to the late Dale Russell, whose work has had a profound impact in North American mosasaur paleontology, Konishi said. But they named the mosasaur for the Everharts, a Kansas couple who have spent more than 30 years sharing their fossils with museums and leading research field trips in the fossil-rich Smoky Hill Chalk.

“We’re still in a little bit of shock at the news. It’s very exciting,” Pamela Everhart said.

“It’s a great honor,” said Mike Everhart, author of “Oceans of Kansas” about mosasaurs and other prehistoric life that inhabited the Western Interior Seaway during the Cretaceous Period.

Mosasaurs are very special to him, he said.

“The oceans would not have been a safe place for swimming in the Cretaceous,” he said. “Mosasaurs were the top predator in the ocean during those times.”

Featured image at top: The teeth of a mosasaur. Photo/Joseph Fuqua II/UC Creative + Brand
Takuya Konishi holds a mosasaur fossil in his office.

UC assistant professor-educator Takuya Konishi studies ancient marine reptiles called mosasaurs. Photo/Joseph Fuqua II/UC Creative + Brand

"""



    
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

#%%
found_entities = []

current = ''
for token in doc:
    if token.ent_type_ == 'PERSON': 
        if token.ent_iob_ == 'B': print(' ')
        print(token.text, end = ' ')
        
#displacy.serve(doc, style="ent")
        
    

    
    
    
        
        
        
        
        


            
             
        
        
     


# https://spacy.io/usage/visualizers
#displacy.serve(doc, style="ent")