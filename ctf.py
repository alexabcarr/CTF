import time
from flask import Flask, request, send_file
import os

os.chdir('/app/files')

ctf = Flask(__name__) 
stage = 0 

template = """

     <html><body><title>{}</title>

         {}<br><br>{}<br><br>{}<br>{}

     </body></html>"""
     
songNames = ['Adam, Check Please', 'Under the Circus Lights', 'Kelly Time', 'Field Notes', 'Sons of Thunder', 'The Tornado', 'Vitamin Sea', 'Dinosaur Park', 'Learn How To Surf', 'The Meadow Lark', 'My Muse']
songNames2 = ['adam-check-please', 'under-the-circus-lights', 'kelly-time', 'field-notes', 'sons-of-thunder', 'the-tornado', 'vitamin-sea', 'dinosaur-park', 'learn-how-to-surf', 'the-meadow-lark', 'my-muse']

passFile = open("passwords.txt", "r") 
passwords = passFile.readlines() 
for p in range(len(passwords)): 
    passwords[p]=passwords[p].strip() 

@ctf.route('/lyrics/<song>')
def return_lyrics(song):
	if song=='all':
		retPage = '<html><body><title>Lyrics for all songs</title>'
		for x in range(len(songNames)):
			retPage+="<a href='/lyrics/{}'>{}</a><br>".format(songNames2[x], songNames[x])
		retPage+='</body></html>'
		return retPage
	try:
		f = open(song+'.txt', 'r')
		lyrics = f.readlines()
		formattedLyrics = '<html><body><title>Lyrics for: {}</title>'.format(songNames[songNames2.index(song)])
		for lin in lyrics:
			formattedLyrics+=lin+'<br>'
		f.close()
		formattedLyrics+='</body></html>'
		return formattedLyrics
		#return send_file(song+'.txt')
	except Exception as e:
		return str(e)


@ctf.route('/play-mp3/<songNum>')
def return_mp3(songNum):
	try:
		return send_file(songNum+'.mp3')
	except Exception as e:
		return str(e)



@ctf.route('/')
def hello(): 
    try:
    	pw = request.args['pw']
    except:
    	pw = ''
    retstr = pw + '' + str(passwords)
    #return(retstr)
    try:
    	hint = request.args['hint']
    except:
    	hint = 'F'
    try:
    	stage = passwords.index(pw)+1
    except:
    	stage = 0
    playSong = ''
    songFiles = []
 
    descFile = open("stage{}.txt".format(stage), 'r')
    stageDesc = descFile.read() 
    descFile.close()
    if not hint=='F':
    	try:
    		helpFile = open('hint{}.txt'.format(stage), 'r')
    		stageHelp = helpFile.read()
    		helpFile.close()
    	except:
    		stageHelp = "There is no hint associated with this stage :)" 
    else:
    	stageHelp = ''
    if pw:
    	curpw = 'The currently entered password is: \'{}\''.format(pw)#, and the required password is \'{}\''.format(pw, passwords[stage])
    else:
    	curpw=''
    	
    try:
    	songReqs = request.args['song']
    	playSong = 'Click a song to play in a new tab: <br>'
    	if songReqs=='all':
    		songReqs='1,2,3,4,5,6,7,8,9,10,11'
    	for song in songReqs.split(','): 
    		try:
    			song = int(song)
    			if song>0 and song<12:
    				songFiles.append(str(song))
    		except:
    			pass
    	for song in songFiles:
    		header = "{}: {}".format(song,songNames[int(song)-1])
    		playSong += "<a href=/play-mp3/"+song+" target='_blank'> Play "+header+"</a><br>"
    		#playSong+=header#+send_file('4.mp3')#"""<audio controls>
    			#<source src=/play-mp3/ type="file/mpeg">
    			#Unsupported element.
    		#</audio><br>"""
    except:
    	playSong = ''
    title = 'Stage {}'.format(stage)
    if stage==5:
    	title= 'Need a hint?'
    if len(stageHelp)>0:
    	title+=' (with hint)'
    	if stage==5:
    		title='Congratulations!'
    toDisplay = template.format(title, stageDesc, stageHelp, playSong,  curpw)
    return toDisplay

