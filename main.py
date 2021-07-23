from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from random import *

#GUI Build
class MyGridLayout(GridLayout):
	#Labels and Button Setup
	def __init__(self, **kwargs):
		super(MyGridLayout,self).__init__(**kwargs)

		#The following code nearly brought me tears and 90% of it
		#I don't have a clue if it even works. I just slapped it in.
		self.cols = 1

		#Labels and buttons
		self.add_widget(Label(text="Number of Attackers: ",
			size_hint_y=None,
			height=30))
		self.attack=TextInput(hint_text="Attack", multiline=False,
			size_hint_y=None,
			height=30)
		self.add_widget(self.attack)

		self.add_widget(Label(text="Number of Defenders: ",
			size_hint_y=None,
			height=30))
		self.defend=TextInput(hint_text="Defend",multiline=False,
			size_hint_y=None,
			height=30)
		self.add_widget(self.defend)

		self.add_widget(Label(text="Number of Rolls: ",
			size_hint_y=None,
			height=30))
		self.roller=TextInput(hint_text="Roll",multiline=False,
			size_hint_y=None,
			height=30)
		self.add_widget(self.roller)

		#Middle Grid Layout
		self.mid_grid=GridLayout()
		self.mid_grid.cols=1
		self.add_widget(self.mid_grid)

		alpha=Label(text="",
			size_hint_y=None,
			height=30)
		self.mid_grid.add_widget(alpha)
		self.ids['offence']=alpha

		bravo=Label(text="",
			size_hint_y=None,
			height=30)
		self.mid_grid.add_widget(bravo)
		self.ids['defence']=bravo

		#Middle Grid Layout
		self.bot_grid = GridLayout()
		self.bot_grid.cols=3
		self.add_widget(self.bot_grid)
		
		self.Instant=Button(text='Instant',
			size_hint_y=None,
			height=30)
		self.Instant.bind(on_press=self.clc)
		self.bot_grid.add_widget(self.Instant)

		self.One_Roll=Button(text='One Roll',
			size_hint_y=None,
			height=30)
		self.One_Roll.bind(on_press=self.clc2)
		self.bot_grid.add_widget(self.One_Roll)

		self.Num_Roll=Button(text='Number Roll',
			size_hint_y=None,
			height=30)
		self.Num_Roll.bind(on_press=self.clc3)
		self.bot_grid.add_widget(self.Num_Roll)

	#First calculation
	def clc(self, instance):
		try:
			at=int(self.attack.text)
			de=int(self.defend.text)
		except:
			at=0
			de=0
		while at >= 2 and de >= 0:
			at -= choice(range(0,3))
			de -= choice(range(0,3))
		if at <= 0:
			alpha= "Attacking side has", str(1), "unit left."
		else:
			alpha="Attacking side has", str(at), "units left."
		if de <= 0:
			bravo="Defending side has", str(0), "unit left."
		else:
			bravo="Defending side has", str(de), "units left."

		self.ids.offence.text=str(alpha).replace('\'','').replace(',','').replace('(','').replace(')','')
		self.ids.defence.text=str(bravo).replace('\'','').replace(',','').replace('(','').replace(')','')

	#Second calculation type
	def clc2(self, instance):
		try:
			at=int(self.attack.text)
			de=int(self.defend.text)
		except:
			at=0
			de=0
		atode=choice(range(1,4))
		other=True
		while other==True:
			if atode==1:
				at -= 2
			elif atode==2:
				at -= 1
				de -= 1
			else:
				de -= 2
			break
		if at <= 0:
			alpha= "Attacking side has", str(1), "unit left."
		else:
			alpha="Attacking side has", str(at), "units left."
		if de <= 0:
			bravo="Defending side has", str(0), "unit left."
		else:
			bravo="Defending side has", str(de), "units left."

		self.ids.offence.text=str(alpha).replace('\'','').replace(',','').replace('(','').replace(')','')
		self.ids.defence.text=str(bravo).replace('\'','').replace(',','').replace('(','').replace(')','')

	#Third calculation type
	def clc3(self,instance):
		try:
			at=int(self.attack.text)
		except:
			at=0
		try:
			de=int(self.defend.text)
		except:
			de=0
		try:
			ro=int(self.roller.text)
		except:
			ro=10
		other=True
		count=0
		while other==True and count<=ro:
			count += 1
			atode=choice(range(1,4))
			if atode==1:
				at -= 2
			elif atode==2:
				at -= 1
				de -= 1
			else:
				de -= 2
		if at <= 0:
			alpha= "Attacking side has", str(1), "unit left."
		else:
			alpha="Attacking side has", str(at), "units left."
		if de <= 0:
			bravo="Defending side has", str(0), "unit left."
		else:
			bravo="Defending side has", str(de), "units left."

		self.ids.offence.text=str(alpha).replace('\'','').replace(',','').replace('(','').replace(')','')
		self.ids.defence.text=str(bravo).replace('\'','').replace(',','').replace('(','').replace(')','')


#Application opening command
class MainApp(App):
	def build(self):
		return MyGridLayout()

#Not sure what this is but all the other guys were doing it
if __name__=='__main__':
	#This makes the thing go. Hopefully.
	MainApp().run()