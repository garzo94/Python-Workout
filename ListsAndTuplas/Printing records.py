import operator
def format_sort_records(people):
   output = []
   # "{1:10} --> one means that placing the value of index 1, with a lengh of 10 characters"
   template = "{1:10} {0:10} {2:5.2f}"
   for person in sorted(people, key=operator.itemgetter(1,0)):
  # person here is a tuple fo name, last and time
       output.append(template.format(*person))

   # ['Putin      Vladimir    3.63', 'Trump      Donald      7.85', 'Xi         Jinping    10.60'] output
   return output

PEOPLE = [('Donald', 'Trump', 7.85),
('Vladimir', 'Putin', 3.626),
('Jinping', 'Xi', 10.603)]

print('\n'.join(format_sort_records(PEOPLE)))

