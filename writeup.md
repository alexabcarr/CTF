Stage 1:
	1. (Terminal 1)cewl localhost:8000/lyrics/all -m 8 --lowercase
		a. vacation, beautiful, dinosaur
	2. crunch x x -o pass.txt -p vacation beautiful dinosaur 
	3. hydra -l ayoung -P pass.txt ftp://192.168.20.7
		a. Password is beautifuldinosaurvacation
Stage 2:
	1. (Terminal 1)cd /shared/Stage2
	2. get dinosaurpark.raw
	3. (Terminal 2)recoverjpeg dinosaurpark.raw
	4. Examine image00007.jpg ‘s EXIF data, specifically the ImageDescription field
		a. Password is RapidCitySDakota
Stage 3:
	1. (Terminal 1)cd ../Stage3
	2. get .occ.txt
	3. get .util.py
	4. get ooc.txt
	5. (Terminal 2) nano uti.py
	6. key = ‘’ -> key = ‘und3rth3’
	7. hint= open(“”,””) -> hint= open(“ooc.txt”,”r”)
	8. add ‘enc = hint.read()’ below
	9. ctrl+x -> y -> enter
	10. python3 uti.py
		a. Prints out the password, ‘c1rcusl1ghts’
Stage 4: ciphertext is vohyvyxymbiaffrrj
	1. (Terminal 1)cd ../Stage4
	2. get songlist.txt
	3. (Terminal 2)nano songlist.txt
	4. Input the potential passwords using the ciphertext however you like 
		a. The correct password is sonsofthunder
		b. The final password is ‘daughtersofwonder’
You’re done! When you ask for a hint, the web page should display the final password, SDaT{c0c0-m00n}
