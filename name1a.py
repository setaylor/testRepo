# Create sets for female and male names
female = set()
f = open("dist.female.first")
for line in f:
  female.add(line.split()[0])
f.close()

male = set()
f = open("dist.male.first")
for line in f:
  male.add(line.split()[0])
f.close()

# Summarize information about the reference data
count = (len(female), len(male))
print "There are %s female names and %s male names." % count
print "There are %s names that appear in both sets." % len(female & male)

# Test data
names = ["PETER", "LOIS", "STEWIE", "BRIAN", "MEG", "CHRIS"]

# Try our algorithm
for name in names:
  if name in male:
    ret = "M"
  elif name in female:
    ret = "F"
  else:
    ret = "NA"
  print "%s: %s" % (name, ret)
