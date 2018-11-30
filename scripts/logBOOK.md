logBOOK
---



# todo

* [ ] implementation of hand gesture 
	* https://gogul09.github.io/software/hand-gesture-recognition-p1
	* https://github.com/Gogul09/gesture-recognition/blob/master/part1.py

	added: Fri 30 Nov 13:59:37 GMT 2018



* [ ] revise openCV issues and references 
	to make filters that are robust to change in 
	different light settings

	added: Fri 30 Nov 00:44:00 GMT 2018



* [ ] fix the base to avoid
	any problems for picking the bricks.

	added: Fri 16 Nov 06:48:04 GMT 2018

* [ ] check where exactly to put the bricks 
	added: Fri 30 Nov 00:44:30 GMT 2018


* [ ] create global variables in `detection.py` for

	```
	area_threshold=2000 # this threshold migth change according to light conditions
        tts.say("I see a LEGO piece")
	```
	
	ADDED: Fri  9 Nov 11:16:14 GMT 2018


* [ ] Would be good to rename 
	Hand.py and hand function in `detection.py` !
	It is confusing which is the purpose of each one!
	maybe hand function as `findinghand`

	ADDED: Fri  9 Nov 12:20:49 GMT 2018


* [ ]  Import common libraies in `__init__.py`
	for all fucntions.
	added: Fri 16 Nov 16:44:44 GMT 2018



# sorted

* [x] code works for c1 and c2 only
	added: Fri 16 Nov 14:06:26 GMT 2018

	now with other positions 
	sorted: Fri 30 Nov 00:38:13 GMT 2018


* [x] issues with no object for image were solved by 
	rebooting NAO machine!


terminal output
```
$ python nao-main.py 
[I] 20159 qimessaging.session: Session listener created on tcp://0.0.0.0:0
[I] 20159 qimessaging.transportserver: TransportServer will listen on: tcp://147.188.136.86:38860
[I] 20159 qimessaging.transportserver: TransportServer will listen on: tcp://169.254.52.160:38860
[I] 20159 qimessaging.transportserver: TransportServer will listen on: tcp://127.0.0.1:38860
Speech recognition engine started
 -3.0
Speech recognition engine started
Blue 0.44549998641
Blue
('I have seen/heard a:', 'Blue')
Traceback (most recent call last):
  File "nao-main.py", line 161, in <module>
    main(args.ip, args.port)
  File "nao-main.py", line 44, in main
    nao_collaboration(IP,PORT,tts)
  File "nao-main.py", line 146, in nao_collaboration
    finish_flag=supermain(IP,PORT,LH,LS,LV,UH,US,UV)	        
  File "nao-main.py", line 59, in supermain
    target=detection.target(IP,PORT,LH,LS,LV,UH,US,UV,tts,showingimage=True)
  File "/home/map479/github/hhcd/scripts/detection.py", line 54, in target
    image=getframe(IP,PORT)
  File "/home/map479/github/hhcd/scripts/detection.py", line 41, in getframe
    array = naoImage[6]
TypeError: 'NoneType' object has no attribute '__getitem__'
```


sorted: Fri 30 Nov 11:18:26 GMT 2018


