import subprocess
from datetime import datetime
 # Prepare host and results file
with open('/Users/neildafarrar/Desktop/t1.txt','r') as hostlist, open('/Users/neildafarrar/Desktop/t2.txt','a') as output:
    #host = Open_host.readline()
    # while loop:  trace route for each host
    for host in hostlist:
        host=host.strip()
        #Write_results.write(line)
        print (host)
        output.write(datetime.now().strftime('%Y/%m/%d %H:%M:%S')+"\n")
        Traceroute = subprocess.Popen(["traceroute", "-m","20", host],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while True:
            hop = Traceroute.stdout.readline()
            if not hop: break
            print ('-->',hop.strip())
            output.write(hop.decode('utf-8')+"\n")
            Traceroute.wait()
output.write("============================================================")
hostlist.close()
output.close()