example_string = '''
IF it be of  importance to the interells of letters, that the vera has been 
afcertained when the compofitions of the Greeks firif abandoned rhythm, 
and afumed the form called afterward in their own language 7E,oq T4ac, 
oratio foluta; the tracing to its fource that branch of the poctic art, 
difIinguitlied by the name of rhimc, will be found an ohhjc(t not uii 
worthy of learned curiof ty ; and the difcuulion, perhaps, may be procduc 
tive of fome collateral obfervations not unprofitable to the caufe of phi.. 
lology in general. 

A z A celebrated 

This content downloaded from 134.226.252.155 on Sat, 22 Jun 2013 15:34:17 PM
All use subject to JSTOR Terms and Conditions

It may be Paid, (for what filly argument bath not bcctl urged iu 
every age by the idle and illiterate ? that verbal invefligations, fuch as 
the prefent, are attended with no folid advantage, are too inconfiderable 
for popular regard, and too remote from general utility. It is anfwered, 
that the moif important difquifitions are often the molt unintere?ing to 
the multitude ; but, for that very reafon, become the more valuable 
to the few for whom they were intcndcd. To underrate a fubje&, be' 
eaufe it happens not to fall in with our own particular fludies orP ur.. 
fuits, is the fore f gn of a narrow and prcjudiced mind. Poetry em 

This content downloaded from 134.222.222.222 on Mon, 12 Jul 2113 15:34:17 PM
All use subject to JSTOR Terms and Conditions


ploys a language of her own, and addreffcs not herfelf to the vulgar: 
through her, every grace of literature, every intelligence of fcienee, cones 
to us recommended, embellithed, illumined : and this academy, when it di 
recged the prefent enquiry, sacrificed at her lhrine, and added another leaf 
to her . laurel. 

This content downloaded from 134.226.252.155 on Sat, 22 Jun 2013 15:34:17 PM
All use subject to JSTOR Terms and Conditions

'''
#assume that the jstor line is on its own
for line in example_string.splitlines():
    if not (line.startswith('This content downloaded from') or
            line.startswith('All use subject to JSTOR Terms and Conditions')):
        print line
    else:
        print 'line removed'


