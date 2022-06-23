print 'Starting Mad Libs, Woohoo!'

name = raw_input('What is your name?')

#a-adjective
a_1= raw_input('Hello! Please enter an Adjective. This can be a word used to describe something! It can be a feeling or a color!')
a_2=raw_input('Enter another Adjective:')
a_3=raw_input('And another Adjective:')

#v-verb
v_1= raw_input ('Okay, Great! Now Enter a Verb. A verb is any word that is an action such as running or hopping or writing!')
v_2=raw_input('And another Verb:')
v_3=raw_input('One more Verb:')

#n-noun
n_1=raw_input('Awesome! Now for a Noun! Please enter a word that is a person, place or thing.')
n_2=raw_input('And another Noun:')
n_3=raw_input('And another Noun:')
n_4=raw_input('Last Noun!')

#t-weird thing
t_1= raw_input('Name an animal that pops into your head!')
t_2=raw_input('What is your favorite food?')
t_3=raw_input('Give the name of a fruit that you despise!')
t_4=raw_input('Enter a number:')
t_5=raw_input('Who is your favorite Superhero?')
t_6=raw_input('Name a country:')
t_7=raw_input('We know you have a sweet tooth! Tell us your favorite dessert!')
t_8=raw_input('Give us a Year:')

print "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %s very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world." % (a_1, name, v_1, a_2, n_1, n_2, t_1, t_2, v_2, n_3, t_3, a_3, name, v_3, t_4, name, t_5, t_5, name, t_6, name, t_7, name, t_8, n_4)