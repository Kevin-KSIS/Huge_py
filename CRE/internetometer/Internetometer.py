from sys import argv
from InternetBot import Run




def chunkIt(seq, num):
	avg = len(seq) / float(num)
	out = []
	last = 0.0
	while last < len(seq):
		out.append(seq[int(last):int(last + avg)])
		last += avg
	return out

if __name__ == "__main__":
    if len(argv) != 4:
            print "Usage:"
            print argv[0] + " <proxylist> <link> <threads>"
            
    else:
            proxy_list = [a.replace('\n','').replace('\r','') for a in \
                  open(argv[1]).readlines()]
            link = argv[2]
            threads = int(argv[3])
            proxy_list = chunkIt(proxy_list, threads)
            for i in proxy_list:
                Run(i, link).run()

    
    
                
            
        
