from tkinter import *
root = Tk()
root.title("Chatbot")
def send():
    send = e.get()
    txt.insert(END,send)
    user = e.get().lower()
    if(user == "hello"):
        txt.insert(END,"Bot -> Hi \n")
    elif(user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END,"Bot -> Hello,Welcome to Intellecto Global...how can i help you? \n")
    elif(e.get() == "how are you"):
        txt.insert(END,"Bot -> fine! and you? \n")
    elif(user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END,"Bot -> Great! how can I help you.\n")
    elif(user == "python"):
        txt.insert(END,"Bot -> python is a software for the modern days.It is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects..To download the latest version of python click the link below...https://www.python.org/downloads/release/python-3102/ \n")
    elif(user == "github"):
        txt.insert(END,"Bot -> GitHub, Inc. is a provider of Internet hosting for software development and version control using Git. It offers the distributed version control and source code management (SCM) functionality of Git, plus its own features. It provides access control and several collaboration features such as bug tracking, feature requests, task management, continuous integration and wikis for every project..To access the github you can head to the link...https://github.com \n")
    elif(user == "oracle"):
        txt.insert(END,"Bot -> An Oracle database is a collection of data treated as a unit. The purpose of a database is to store and retrieve related information. A database server is the key to solving the problems of information management..you can download the latest version of oracle here...https://download.oracle.com/otn-pub/otn_software/db-express/OracleXE213_Win64.zip \n")
    elif(user == "django"):
        txt.insert(END,"Bot -> Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Built by experienced developers, Django takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It is free and open source, has a thriving and active community, great documentation, and many options for free and paid-for support.\n")
    elif(user == "slack"):
        txt.insert(END,"Bot -> Slack is a messaging app for business that connects people to the information that they need. By bringing people together to work as one unified team, Slack transforms the way that organisations communicate. \n")
    elif(user == "textnow"):
        txt.insert(END,"Bot -> textnow is a necessary app which helps you create a second number and can be able to access or make calls throughout the world,it connects people with data for free of cost in some specified regions..to get the latest version of textnow .exe click on.....https://www.textnow.com/downloads \n")
    elif(user == "scrum"):
        txt.insert(END,"Bot -> scrum meeting is the meeting where all the co-workers gathers together and share their update till the day,it also helps in making good bond and also empowers people \n")
    elif(user == "bye"):
        txt.insert(END,"Bot -> see you again! have a good day ")
    else:
        txt.insert(END,"Bot -> Sorry! I dind't got you \n")
    e.delete(0, END)
txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1, column=0)
send = Button(root, text="Send", command=send).grid(row=1, column=1)
root.mainloop()