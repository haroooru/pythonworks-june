#writing operations

f=open("k.txt","w")
#if file already exist it creates emty file

f.write("hello")

sample_paragraph=""""A user who randomly clicks links with a chance of jumping to any page."

 Explanation:
The random surfer model is a foundational concept in the PageRank algorithm, which ranks web
 pages based on their link structure. It assumes:

A user (the "random surfer") clicks on links at random.

Occasionally, the user may jump to any page on the web, not just those
 linked from the current page.

This jump probability prevents the algorithm from getting stuck in dead ends 
or loops, ensuring a more robust and fair ranking system.

If you're modeling web behavior or building a graph-based ranking system 
for your hackathon, I can help simulate this with Python or visualize it in your workflow."""
f.write(sample_paragraph)
f.close()
# write multiple lines into file

f=open("k.txt","w")   #open file in write mode

content=['python\n','java\n','php\n']   #list of lines

f.writelines(content)   #writes list into file
f.close()               #close file
