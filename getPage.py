# -*- coding: utf-8 -*-
import urllib.request
import time

def RateLimited(minInterval):
    #the decorate of python
    #can limit the interval between two request
    def decorate(func):
        lastTimeCalled = [0.0]
        def rateLimitedFunction(*args,**kargs):
            elapsed = time.time() - lastTimeCalled[0]
            leftToWait = minInterval - elapsed
            if leftToWait>0:
                time.sleep(leftToWait)
            ret = func(*args,**kargs)
            lastTimeCalled[0] = time.time()
            return ret
        return rateLimitedFunction
    return decorate

@RateLimited(3)            
def get(req,retries,encoding = None):
	print("in getPage.get")
	try:
		response = urllib.request.urlopen(req)
		byte = response.read()
	except Exception:
		if retries > 0:
			return get(req,retries - 1,encoding)
		else:
			print ('Get Failed',req)
			return None
	try:
		strs = byte.decode(encoding,'ignore')
	except Exception:
		print("coding Exception")
		return None
	return strs

if __name__ == '__main__':
    req = 'http://www.lovebanker.com/category/bank'
    chunk =get(req, 3, 'utf-8')
    print (chunk)
    
