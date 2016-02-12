'''Maggie Borkowski
Programming for COGS & AI
Final Project'''

import pygame
import random
import time,datetime,os

colors = {
        'black': [ 0, 0, 0],
        'white': [255,255,255],
        'blue ': [ 0, 0,255],
        'green': [ 0,255, 0],
        'red':   [255, 0, 0]
        }

def getDateTimeStamp():
    d = datetime.datetime.now().timetuple()
    return "%d-%02.d-%02.d_%02.d-%02.d-%02.d" % (d[0], d[1], d[2], d[3], d[4], d[5])
     

class World():
    stop = False
    
    def __init__(self):
        pygame.init()
        resolution = [1000, 500]
        self.screen = pygame.display.set_mode(resolution) # returns a Surface
        pygame.display.set_caption("Final Project")
        self.font = pygame.font.Font(None, 30)
        self.timer = pygame.time.Clock()
        
    def process_events(self, question):
    	res = 'none'
    	numholder = ''
        while res == 'none':
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    res = 'done'
                elif question < 6 and question > 0:
                	#reading question, waits for user to hit a, b, c, or d
                	if event.key == pygame.K_a:
	                  res = 'a'
	                elif event.key == pygame.K_b:
	                  res = 'b'
	                elif event.key == pygame.K_c:
	                  res = 'c'
	                elif event.key == pygame.K_d:
	                  res = 'd'
	                self.timer.tick()
                else:
                	#math question or instruction screen
                	if event.key != pygame.K_RETURN:

                        #concatenates every keystroke into response until user hits enter
                		numholder += pygame.key.name(event.key)
                		print numholder
                	else:
                		res = numholder
                		self.timer.tick()
                
        return(res)

    #displays appropriate text for each question    
    def display_stimulus(self,test,question):
    	# 0 = reading instructions
        # 1-5 = reading questions, 3 per question because of 3 different tests
        # 6 = math instructions
    	# 7-11 = math questions

        self.screen.fill(colors['white'])

        if question == 0:
        	textImg1 = self.font.render( 'Please take two minutes to read the provided article.', 1, colors['black'])
        	textImg2 = self.font.render( 'When you have finished, hit Enter.', 1, colors['black'])
        	textImg3 = self.font.render( 'You will be asked several multiple choice questions about the article.', 1, colors['black'])
        	textImg3 = self.font.render( 'For each question, enter your answer (a, b, c, or d) on the keyboard.', 1, colors['black'])
        	textImg4 = self.font.render( 'Answer as quickly as you can while still maintaining high accuracy.', 1, colors['black'])
        	self.screen.blit(textImg1,(100,100))
        	self.screen.blit(textImg2,(100,150))
        	self.screen.blit(textImg3,(100,200))
        	self.screen.blit(textImg4,(100,250))

        elif question == 1:
        	if test == 1:
        		textImg = self.font.render( 'The word \"legacy\" (line 4) most closely means:', 1, colors['black'])
        		aImg = self.font.render( 'a) endowed', 1, colors['black'])
        		bImg = self.font.render( 'b) untenable', 1, colors['black'])
        		cImg = self.font.render( 'c) traditional', 1, colors['black'])
        		dImg = self.font.render( 'd) reputable', 1, colors['black'])
        		self.screen.blit(textImg,(100,100))
        		self.screen.blit(aImg,(100,150))
        		self.screen.blit(bImg,(100,200))
        		self.screen.blit(cImg,(100,250))
        		self.screen.blit(dImg,(100,300))
        	elif test == 2:
        		textImg = self.font.render( 'The word \"synthesizing\" (line 6) most closely means:', 1, colors['black'])
        		aImg = self.font.render( 'a) manufacturing', 1, colors['black'])
        		bImg = self.font.render( 'b) analyzing', 1, colors['black'])
        		cImg = self.font.render( 'c) amalgamating', 1, colors['black'])
        		dImg = self.font.render( 'd) standardizing', 1, colors['black'])
        		self.screen.blit(textImg,(100,100))
        		self.screen.blit(aImg,(100,150))
        		self.screen.blit(bImg,(100,200))
        		self.screen.blit(cImg,(100,250))
        		self.screen.blit(dImg,(100,300))
        	else:
        		#test = 3
        		textImg = self.font.render( 'The word \"synthetic\" (line 15) most closely means:', 1, colors['black'])
        		aImg = self.font.render( 'a) inorganic', 1, colors['black'])
        		bImg = self.font.render( 'b) makeshift', 1, colors['black'])
        		cImg = self.font.render( 'c) composite', 1, colors['black'])
        		dImg = self.font.render( 'd) structured', 1, colors['black'])
        		self.screen.blit(textImg,(100,100))
        		self.screen.blit(aImg,(100,150))
        		self.screen.blit(bImg,(100,200))
        		self.screen.blit(cImg,(100,250))
        		self.screen.blit(dImg,(100,300))
        	
        elif question == 2:
        	if test == 1:
        		textImg1 = self.font.render( 'The author would agree that all of the following contribute', 1, colors['black'])
        		textImg2 = self.font.render( 'to the gender gap in math and reading except:', 1, colors['black'])
        		aImg = self.font.render( 'a) biological differences', 1, colors['black'])
        		bImg = self.font.render( 'b) socio-economic conditions', 1, colors['black'])
        		cImg = self.font.render( 'c) educational techniques', 1, colors['black'])
        		dImg = self.font.render( 'd) cultural stereotypes', 1, colors['black'])
        		self.screen.blit(textImg1,(100,100))
        		self.screen.blit(textImg2,(100,150))
        		self.screen.blit(aImg,(100,200))
        		self.screen.blit(bImg,(100,250))
        		self.screen.blit(cImg,(100,300))
        		self.screen.blit(dImg,(100,350))

        	elif test == 2:
        		textImg1 = self.font.render( 'The author would agree that all of the following contribute to', 1, colors['black'])
        		textImg2 = self.font.render( 'the perpetuated belief in a math and reading gender gap except:', 1, colors['black'])
        		aImg = self.font.render( 'a) more men in science careers', 1, colors['black'])
        		bImg = self.font.render( 'b) gender stereotyping', 1, colors['black'])
        		cImg = self.font.render( 'c) cultural expectations', 1, colors['black'])
        		dImg = self.font.render( 'd) biological differences', 1, colors['black'])
        		self.screen.blit(textImg1,(100,100))
        		self.screen.blit(textImg2,(100,150))
        		self.screen.blit(aImg,(100,200))
        		self.screen.blit(bImg,(100,250))
        		self.screen.blit(cImg,(100,300))
        		self.screen.blit(dImg,(100,350))
        	else:
        		#test = 3
        		textImg = self.font.render( 'The author would agree with all of the following except:', 1, colors['black'])
        		aImg = self.font.render( 'a) researching the application of computers to creative fields is valuable', 1, colors['black'])
        		bImg = self.font.render( 'b) PaleoDeepDive is an impressive accomplishment', 1, colors['black'])
        		cImg = self.font.render( 'c) the use of computers in the place of humans is desirable', 1, colors['black'])
        		dImg = self.font.render( 'd) the Paleobiology Database is easy to sort', 1, colors['black'])
        		self.screen.blit(textImg,(100,100))
        		self.screen.blit(aImg,(100,150))
        		self.screen.blit(bImg,(100,200))
        		self.screen.blit(cImg,(100,250))
        		self.screen.blit(dImg,(100,300))

        elif question == 3:
        	if test == 1:
        		textImg = self.font.render( 'It is implied that the \"sociological rationalizations\" (line 6) are:', 1, colors['black'])
        		aImg = self.font.render( 'a) unfounded', 1, colors['black'])
        		bImg = self.font.render( 'b) imperative', 1, colors['black'])
        		cImg = self.font.render( 'c) trenchant', 1, colors['black'])
        		dImg = self.font.render( 'd) alarming', 1, colors['black'])
        		self.screen.blit(textImg,(100,100))
        		self.screen.blit(aImg,(100,150))
        		self.screen.blit(bImg,(100,200))
        		self.screen.blit(cImg,(100,250))
        		self.screen.blit(dImg,(100,300))
        	elif test == 2:
        		textImg = self.font.render( 'It is implied that the \"gender expectations\" (line 29) are:', 1, colors['black'])
        		aImg = self.font.render( 'a) harmful', 1, colors['black'])
        		bImg = self.font.render( 'b) unintentional', 1, colors['black'])
        		cImg = self.font.render( 'c) scientific', 1, colors['black'])
        		dImg = self.font.render( 'd) conspicuous', 1, colors['black'])
        		self.screen.blit(textImg,(100,100))
        		self.screen.blit(aImg,(100,150))
        		self.screen.blit(bImg,(100,200))
        		self.screen.blit(cImg,(100,250))
        		self.screen.blit(dImg,(100,300))
        	else:
        		#test = 3
        		textImg = self.font.render( 'It is implied that a task in the \"subjective camp\" (line 8) is:', 1, colors['black'])
        		aImg = self.font.render( 'a) more difficult than other tasks', 1, colors['black'])
        		bImg = self.font.render( 'b) more interesting than other tasks', 1, colors['black'])
        		cImg = self.font.render( 'c) more creative than other tasks', 1, colors['black'])
        		dImg = self.font.render( 'd) more mundane than other tasks', 1, colors['black'])
        		self.screen.blit(textImg,(100,100))
        		self.screen.blit(aImg,(100,150))
        		self.screen.blit(bImg,(100,200))
        		self.screen.blit(cImg,(100,250))
        		self.screen.blit(dImg,(100,300))

        elif question == 4:
        	if test == 1:
        		textImg = self.font.render( 'Gijsbert Stoet believes that Sweden:', 1, colors['black'])
        		aImg = self.font.render( 'a) has worked hard on its educational system', 1, colors['black'])
        		bImg = self.font.render( 'b) has successfully reduced gender gap problems', 1, colors['black'])
        		cImg = self.font.render( 'c) has neglected boys\' reading skills', 1, colors['black'])
        		dImg = self.font.render( 'd) has poor socio-economic conditions', 1, colors['black'])
        		self.screen.blit(textImg,(100,100))
        		self.screen.blit(aImg,(100,150))
        		self.screen.blit(bImg,(100,200))
        		self.screen.blit(cImg,(100,250))
        		self.screen.blit(dImg,(100,300))
        	elif test == 2:
        		textImg = self.font.render( 'Janet Shibley Hyde believes that girls:', 1, colors['black'])
        		aImg = self.font.render( 'a) are better at math than boys', 1, colors['black'])
        		bImg = self.font.render( 'b) are better at reading than boys', 1, colors['black'])
        		cImg = self.font.render( 'c) are equally capable as compared to boys', 1, colors['black'])
        		dImg = self.font.render( 'd) are better and both math and reading than boys', 1, colors['black'])
        		self.screen.blit(textImg,(100,100))
        		self.screen.blit(aImg,(100,150))
        		self.screen.blit(bImg,(100,200))
        		self.screen.blit(cImg,(100,250))
        		self.screen.blit(dImg,(100,300))
        	else:
        		#test = 3
        		textImg = self.font.render( 'Shanan Peters believes that PaleoDeepDive:', 1, colors['black'])
        		aImg = self.font.render( 'a) can determine the meaning of most catalogued statements', 1, colors['black'])
        		bImg = self.font.render( 'b) should be used for any size of database', 1, colors['black'])
        		cImg = self.font.render( 'c) has an advantage over humans with large data sets', 1, colors['black'])
        		dImg = self.font.render( 'd) will not be useful until the computer tools improve', 1, colors['black'])
        		self.screen.blit(textImg,(100,100))
        		self.screen.blit(aImg,(100,150))
        		self.screen.blit(bImg,(100,200))
        		self.screen.blit(cImg,(100,250))
        		self.screen.blit(dImg,(100,300))

        elif question == 5:
        	if test == 1:
        		textImg = self.font.render( 'Based on the text, Ethiopia, an impoverished country, could be inferred to have:', 1, colors['black'])
        		aImg = self.font.render( 'a) a large reading gap and a large math gap', 1, colors['black'])
        		bImg = self.font.render( 'b) a small reading gap and a large math gap', 1, colors['black'])
        		cImg = self.font.render( 'c) a large reading gap and a small math gap', 1, colors['black'])
        		dImg = self.font.render( 'd) a small reading gap and a small math gap', 1, colors['black'])
        		self.screen.blit(textImg,(100,100))
        		self.screen.blit(aImg,(100,150))
        		self.screen.blit(bImg,(100,200))
        		self.screen.blit(cImg,(100,250))
        		self.screen.blit(dImg,(100,300))
        	elif test == 2:
        		textImg1 = self.font.render( 'Based on the text, what grouping could be inferred to have', 1, colors['black'])
        		textImg2 = self.font.render( 'the most equal gender distribution in math and science careers?', 1, colors['black'])
        		aImg = self.font.render( 'a) first-world countries', 1, colors['black'])
        		bImg = self.font.render( 'b) non-Western countries', 1, colors['black'])
        		cImg = self.font.render( 'c) countries that have worked to eliminate gender stereotypes', 1, colors['black'])
        		dImg = self.font.render( 'd) countries that have rigorous secondary education programs', 1, colors['black'])
        		self.screen.blit(textImg1,(100,100))
        		self.screen.blit(textImg2,(100,150))
        		self.screen.blit(aImg,(100,200))
        		self.screen.blit(bImg,(100,250))
        		self.screen.blit(cImg,(100,300))
        		self.screen.blit(dImg,(100,350))
        	else:
        		#test = 3
        		textImg1 = self.font.render( 'Based on information in the text, which of the following', 1, colors['black'])
        		textImg2 = self.font.render( 'would you expect to be the hardest for a computer to decipher?', 1, colors['black'])
        		aImg = self.font.render( 'a) a spreadsheet of sorted data', 1, colors['black'])
        		bImg = self.font.render( 'b) a list of complex equations', 1, colors['black'])
        		cImg = self.font.render( 'c) a scientific article', 1, colors['black'])
        		dImg = self.font.render( 'd) a programmed script for playing chess', 1, colors['black'])
        		self.screen.blit(textImg1,(100,100))
        		self.screen.blit(textImg2,(100,150))
        		self.screen.blit(aImg,(100,200))
        		self.screen.blit(bImg,(100,250))
        		self.screen.blit(cImg,(100,300))
        		self.screen.blit(dImg,(100,350))

        elif question == 6:
        	textImg1 = self.font.render( 'You will now be presented with several math problems.', 1, colors['black'])
        	textImg2 = self.font.render( 'Type your numeric answer on the keyboard, then hit Enter after each problem.', 1, colors['black'])
        	textImg3 = self.font.render( 'Simplify your answers and use decimals rather than fractions when necessary.', 1, colors['black'])
        	textImg4 = self.font.render( 'Answer as quickly as you can while still maintaining high accuracy.', 1, colors['black'])
        	self.screen.blit(textImg1,(100,100))
        	self.screen.blit(textImg2,(100,150))
        	self.screen.blit(textImg3,(100,200))
        	self.screen.blit(textImg4,(100,250))

        elif question == 7:
        	textImg = self.font.render( '983 + 857 =', 1, colors['black'])
        	self.screen.blit(textImg,(100,100))

        elif question == 8:
        	textImg = self.font.render( '76 x 9 =', 1, colors['black'])
        	self.screen.blit(textImg,(100,100))

        elif question == 9:
        	textImg = self.font.render( '1423 - 515 =', 1, colors['black'])
        	self.screen.blit(textImg,(100,100))

        elif question == 10:
        	textImg = self.font.render( '86 / 4 =', 1, colors['black'])
        	self.screen.blit(textImg,(100,100))

        elif question == 11:
        	textImg = self.font.render( '(3/2) / (3/4) =', 1, colors['black'])
        	self.screen.blit(textImg,(100,100))

        else:
        	#endscreen
        	textImg = self.font.render( 'Thank you for participating! Hit ESC to quit.', 1, colors['black'])
        	self.screen.blit(textImg,(100,100))

        pygame.display.update()
        
    def run(self,S):
        fn = '_'.join(['finalproj',getDateTimeStamp()])
        p = os.path.join(os.getcwd(),'finalprojdata')
        if not os.path.isdir(p): os.mkdir(p)
        path =  p + '/' + fn
        L.open_log(path)
        for i in range(0,13):
            if not self.stop:

                id = S.id
                age = S.age
                gender = S.gender
                test = S.test
                answer = None

                #answer key
                if i==1 or i==4 or i==5:
                	answer = 'c'
                elif i==2:
                	answer = 'd'
                elif i==3:
                	answer = 'a'
                elif i==7:
                	answer = 1840
                elif i==8:
                	answer = 684
                elif i==9:
                	answer = 908
                elif i==10:
                	answer = 21.5
                elif i==11:
                	answer = 2

                self.display_stimulus(test, i)

                #wait for user response
                event = self.process_events(i)
                if event == 'done': 
                    self.stop = True
                else:
                    #log user response & time, unless it's on an instruction screen (see display_stimulus for details)
                	if i!=0 and i!=6 and i!=12:
                		L.log(ID=id, Age=age, Gender=gender, Test=test, Question=str(i)+'\t', Response=event+'\t', C_Answer=str(answer)+'\t', Reaction_Time_ms=self.timer.get_time())
            		

        L.close_log()

class Logger():
    def __init__(self,header,dl = '\t', nl = '\n', fl = 'NA'):
        self.header = header
        self.delim = dl
        self.newline = nl
        self.filler = fl
        self.file = None
        return
        
    def open_log(self,fn):
        self.file = open(fn,'w')
        self.file.write(self.delim.join(self.header))
        self.file.write(self.newline)
        return
        
    def log(self,  **kwargs):
        line = [self.filler] * len(self.header)
        for k, v in kwargs.iteritems():
            if k in self.header:
                line[self.header.index(k)] = str(v)
        self.file.write(self.delim.join(line)) # convert list to delimited string
        self.file.write(self.newline)
        return
        
    def close_log(self):
        self.file.close()
                        
            
class Subject():
    id = None
    age = None
    gender = None
    test = None

    
    def __init__(self):
        self.id = raw_input('Enter Subject ID: ')
        self.age = raw_input('Enter Subject Age: ')
        self.gender = raw_input('Enter Subject Gender (M/F): ')
        #must enter 1, 2, or 3 for self.test
        self.test = int(raw_input('Enter Subject Test: '))
 

if __name__ == "__main__":
    S = Subject()
    L = Logger(['ID', 'Age', 'Gender', 'Test', 'Question', 'Response', 'C_Answer', 'Reaction_Time_ms'])
    W = World()

    W.run(S)