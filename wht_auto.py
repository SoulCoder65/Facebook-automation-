from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import json
import time
from bs4 import BeautifulSoup
from gi.repository import Notify, GdkPixbuf

#For GUI
import datetime
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
from datetime import datetime
class whatapp:
    def __init__(self):
        # Load json data
        with open("config.json") as details:
            self.det=json.load(details)
        # To use chrome cookies to avoid scanning
        self.options=webdriver.ChromeOptions()
        self.options.add_argument('--user-data-dir=.config/google-chrome/Default')
        self.options.add_argument('--profile-directory=Default')
        # self.options.add_argument("--headless")
        self.driver=webdriver.Chrome(executable_path=self.det["webdriver_url"],options=self.options)
        self.driver.get(self.det["website"])

    # Sending MSg to single user
    def send_msg(self,username,msg):
        self.driver.implicitly_wait(25)
        try:
            self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').click() #click on search menu
            self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(username) #Enter name of user
            user=self.driver.find_element_by_xpath('//span[@title="{}"]'.format(username)) #if user found then click on his/her name
            user.click()
            self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(msg) #write msg
            self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click() #click on send icon
            time.sleep(2)
            self.driver.close()
            messagebox.showinfo("Message Sent","Message Sent Successfully")
        except NoSuchElementException:
            messagebox.showerror("Error Occured","User Not found")
        finally:
            self.driver.close()
    # Sending media files
    def send_media_file(self,username,media_path):
        self.driver.implicitly_wait(15)
        try:
            self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').click() #click on search menu
            self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(username) #Enter name of user
            user = self.driver.find_element_by_xpath('//span[@title="{}"]'.format(username)) #if user found then click on his/her name
            user.click()
            self.driver.find_element_by_xpath('//div[@title="Attach"]').click()
            self.driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input').send_keys(media_path)
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div').click()
            time.sleep(3)
            self.driver.close()
            messagebox.showinfo("Sent!!","Image Sent Successfully")
        except NoSuchElementException as e:
            messagebox.showerror("Error Occured","Can't Sent Image Try Agin!")

    # Sending document files
    def send_doc_file(self,filename,username):
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_xpath(
                '//*[@id="side"]/div[1]/div/label/div/div[2]').click()  # click on search menu
            self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(username)  # Enter name of user
            user = self.driver.find_element_by_xpath(
                '//span[@title="{}"]'.format(username))  # if user found then click on his/her name
            user.click()
            self.driver.find_element_by_xpath('//div[@title="Attach"]').click()
            self.driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button/input').send_keys(filename)
            self.driver.implicitly_wait(7)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span').click()
        except NoSuchElementException as e:
            print("Media not found")

    #Change Profile Picture
    def change_prof_pic(self,profile_path):
        self.driver.implicitly_wait(20)
        try:
            self.driver.find_element_by_xpath('//*[@id="side"]/header/div[1]/div/img').click() #click on profile head
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/div/div/div[1]/div/input').send_keys(profile_path) #Send new profile path
            self.driver.implicitly_wait(4)
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/span/div/div/div[2]/span/div/div/span').click() #Click on updat profile icon
            time.sleep(3)
            self.driver.close()
            messagebox.showinfo("Profile Set","Profile Set Successfully")
        except Exception as e:
            messagebox.showerror("Error Occur","Can't Set Profile Picture now try Again!!")
        finally:
            self.driver.close()
    #Change username
    def change_user_name(self,username):
        time.sleep(10)
        try:
            self.driver.find_element_by_xpath('//*[@id="side"]/header/div[1]/div/img').click() #click on profile pic
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/div/div/div[2]/div[2]/div[1]/span[2]/div').click() #click on pencil icon to edit
            self.driver.implicitly_wait(2)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/div/div/div[2]/div[2]/div[1]/div/div[2]').clear() #clear field contain name
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/div/div/div[2]/div[2]/div[1]/div/div[2]').send_keys(username) #Enter new name
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/div/div/div[2]/div[2]/div[1]/span[2]/div/span').click()
            self.driver.close()
            messagebox.showinfo("Name Changed!!", f"Name changed To {username}")
        except Exception as e:
            messagebox.showerror("Error Occur", f"Unable to change name to {username}")
        finally:
            self.driver.close()


    #change status
    def change_status(self,new_status):
        self.driver.implicitly_wait(15)
        try:
            self.driver.find_element_by_xpath('//*[@id="side"]/header/div[1]/div/img').click()  # click on profile pic
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/div/div/div[4]/div[2]/div[1]/span[2]/div/span').click()  # click on pencil icon to edit
            self.driver.implicitly_wait(2)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/div/div/div[4]/div[2]/div[1]/div/div[2]').clear() #clear previous status
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/div/div/div[4]/div[2]/div[1]/div/div[2]').send_keys(new_status)  # Enter new Status
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/div/div/div[4]/div[2]/div[1]/span[2]/div/span').click()
            self.driver.close()
            messagebox.showinfo("Status Set",f"Status set to {new_status}")
        except Exception as e:
            messagebox.showerror("Error Occur",f"Unable To set Status to {new_status}")
        finally:
            self.driver.close()
    #User details
    def user_details(self,username):
        self.driver.implicitly_wait(15)
        try:
            self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').click()  # click on search menu
            self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(username)  # Enter name of user
            user = self.driver.find_element_by_xpath('//span[@title="{}"]'.format(username))  # if user found then click on his/her name
            user.click()
            # time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span').click()  # if user found then click on his/her name
            time.sleep(3)
            status=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[4]/div[2]/div/div/span/span').get_attribute('title')
            char_list = [status[j] for j in range(len(status)) if ord(status[j]) in range(65536)]
            statusSimple = ''
            for j in char_list:
                statusSimple = statusSimple + j
            phone_no=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[4]/div[3]/div/div/span/span').get_attribute("innerHTML")

            common_groups=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[5]/div[2]/div')
            beautify_Details = BeautifulSoup(common_groups.get_attribute('innerHTML'), 'html.parser')
            groups_list=[]
            for i in beautify_Details.findAll('span', {'class': '_3ko75 _5h6Y_ _3Whw5'}):
                groups_list.append(i.text)
            time.sleep(3)
            self.driver.close()
        except Exception:
            messagebox.showerror("Error Occured","Unable To fetch Data")
        # Creating new window to show gathered details
        global result_field_new
        global new_window
        new_window = Toplevel(window_screen)
        new_window.title("Bot Result")
        new_window.geometry("600x450")

        result_field_new = Text(new_window)
        result_field_new.pack()
        result_field_new.config(background='#e8ead3', foreground='#654062', font=("Courier", 13, "bold"))
        result_field_new.insert(END, f"***************Details Of User --{username} *********** \n")
        result_field_new.insert(END,f"Status:- {statusSimple}\n")
        result_field_new.insert(END,f"Phone no:- {phone_no}\n")
        result_field_new.insert(END, "Common Groups\n")
        for i in groups_list:
            result_field_new.insert(END,f"{i}\n")
        exit_btn = Button(new_window, text="Exit", command=exit_new_window)
        exit_btn.pack()

    #read_trial
    def show_msgs(self):
        self.driver.implicitly_wait(15)
        # scroll_page = self.driver.find_element_by_xpath('//*[@id="pane-side"]')  # To scroll page
        try:
            get_chat_details=self.driver.find_elements_by_class_name('_2kHpK')
            no_of_chats_dict=[]
            # For notification
            Notify.init("Whatapp Automation")
            image = GdkPixbuf.Pixbuf.new_from_file("images/whatapp.png")
            for chat_details in get_chat_details:
                chat_detail = BeautifulSoup(chat_details.get_attribute('innerHTML'), 'html.parser')
                sender_name=chat_detail.find("span",{"class":"_3ko75 _5h6Y_ _3Whw5"})
                no_of_chats_class=chat_detail.find("div",{"class":"ZKn2B"})
                # no_of_chats=BeautifulSoup(no_of_chats_class.text,"html.parser")

                if no_of_chats_class:
                    # sum_msgs+=int(no_of_chats_class.text)
                    no_of_chats_dict.append({sender_name.text:no_of_chats_class.text})
                    print(sender_name.text)
                    print(no_of_chats_class.text)
                    # Create the notification object
                    summary = f"You have {no_of_chats_class.text} messages from:"
                    body = sender_name.text
                    notification = Notify.Notification.new(
                        summary,
                        body,  # Optional
                    )
                    notification.set_icon_from_pixbuf(image)
                    notification.show()
                time.sleep(0.5)
            self.driver.close()
        except Exception:
            messagebox.showerror("Error","Unable to get Message Details!!")

#Tkinter Functions
def clear_entry(event, entry):
    entry.delete(0, END)

# To remove popup window
def exit_new_window():
    window_screen.forget(new_window)
#Change_username
def change_user_name():
    wht = whatapp()
    wht.change_user_name(new_user_name_var.get())
    return

#Get userDetails
def user_details():
    wht=whatapp()
    wht.user_details(user_details_var.get())
    return
#Show messages_notification
def check_msgs():
    wht=whatapp()
    wht.show_msgs()
    return

#Change Status
def change_status():
    wht=whatapp()
    wht.change_status(new_status_var.get())
    return

#send images fun
def send_images():
    filename = filedialog.askopenfilename()
    user=send_image_user_var.get()
    wht=whatapp()
    wht.send_media_file(user,filename)
    return

#send doc fun
def send_docs():
    filename = filedialog.askopenfilename()
    user=send_doc_user_var.get()
    wht=whatapp()
    wht.send_doc_file(filename,user)
    return
#send message
def send_msg():
    name=send_msg_user_var.get()
    msg=send_msg_var.get()
    greeting_permission=messagebox.askyesno("Greeting Permission","Should Include Greeting?")
    cur_time=int(datetime.now().strftime("%H"))
    if cur_time>=4 and cur_time<12:
        greet_msg="Good Moring\n"
    elif cur_time>=12 and cur_time<17:
        greet_msg="Good After Noon"
    else:
        greet_msg="Good Evening"
    if greeting_permission:
        wht=whatapp()
        comp_msg=greet_msg+"\n "+msg
        wht.send_msg(name,comp_msg)
        return
    else:
        wht = whatapp()
        wht.send_msg(name,msg)
        return
#change_profile fun
def change_profile():
    filename = filedialog.askopenfilename()
    wht = whatapp()
    wht.change_prof_pic(filename)
    return


if __name__ == '__main__':
    #Tkinter

    window_screen = Tk()
    window_screen.title("WhatsApp Automation")
    window_screen.geometry("750x800")
    window_screen.config(bg='#d6efc7')
    im_temp = Image.open("images/what_back.png")
    im_temp = im_temp.resize((300, 250), Image.ANTIALIAS)
    im_temp.save("images/what_back.png", "png")
    logo_img = ImageTk.PhotoImage(Image.open("images/whatappback.png"))
    logo_label = Label(window_screen, image=logo_img)
    logo_label.grid(row=0, column=0, padx=200, pady=20)
    logo_label.config(background='#d6efc7')

    robot1_img = ImageTk.PhotoImage(Image.open("images/robot1.png"))
    robot1_label = Label(window_screen, image=robot1_img)
    robot1_label.place(x=244,y=10)

    robot2_img = ImageTk.PhotoImage(Image.open("images/robot2.png"))
    robot2_label = Label(window_screen, image=robot2_img)
    robot2_label.place(x=495, y=70)

    # VARIABLES
    new_user_name_var = StringVar()
    new_status_var = StringVar()
    user_details_var = StringVar()
    send_doc_user_var = StringVar()
    send_image_user_var = StringVar()
    send_msg_user_var = StringVar()
    send_msg_var = StringVar()

    #STYLING
    style = Style()

    # FONT
    font = ("Courier", 18, "italic")
    style.configure('TButton', font=
    ('calibri', 10, 'bold',),
                    foreground='#3b6978', background='#f7f5dd', activeforeground='green', activebackground='red',
                    borderwidth='4')
    style.configure('TEntry', foreground='#900c3f')

    style.configure('TLabel', background='#d6efc7', foreground='#2f2519', font=("Courier", 13, "bold") )

    # Fields
    optionsFrame = Label(window_screen)
    optionsFrame.grid(row=1, column=0, sticky="w")
    optionsFrame.config(background='#d6efc7')

    # Changing username
    change_user_nameLabel = Label(optionsFrame, text="Change User name")
    change_user_nameLabel.grid(row=0, column=0, padx=30)
    change_user_name_entry = Entry(optionsFrame, width=30,textvariable=new_user_name_var)
    change_user_name_entry.insert(0, "Enter Name...")
    change_user_name_entry.grid(row=1, column=0, padx=30)
    change_user_name_entry.bind("<Button-1>", lambda event: clear_entry(event, change_user_name_entry))
    change_user_name_btn = Button(optionsFrame, text="Change Name",command=change_user_name)
    change_user_name_btn.grid(row=2, column=0, padx=30, pady=15)

    #Changing Bio
    change_bioLabel = Label(optionsFrame, text="Change Bio/Status")
    change_bioLabel.grid(row=0, column=1, padx=30,pady=10)
    change_bio_entry = Entry(optionsFrame, width=30,textvariable=new_status_var)
    change_bio_entry.insert(0, "Enter New Bio")
    change_bio_entry.grid(row=1, column=1, padx=30)
    change_bio_entry.bind("<Button-1>", lambda event: clear_entry(event, change_bio_entry))
    change_bio_btn = Button(optionsFrame, text="Change Bio/Status",command=change_status)
    change_bio_btn.grid(row=2, column=1, padx=30, pady=15)

    # Send Images
    username_imgLabel = Label(optionsFrame, text="Enter user to send images")
    username_imgLabel.grid(row=3, column=0, padx=30)
    username_img_entry = Entry(optionsFrame, width=30,textvariable=send_image_user_var)
    username_img_entry.insert(0, "User Name")
    username_img_entry.grid(row=4, column=0, padx=30)
    username_img_entry.bind("<Button-1>", lambda event: clear_entry(event, username_img_entry))
    username_imgbtn = Button(optionsFrame, text="Select Image",command=send_images)
    username_imgbtn.grid(row=5, column=0, padx=30, pady=15)

    # Send Documents
    username_docLabel = Label(optionsFrame, text="Enter user to send document")
    username_docLabel.grid(row=3, column=1, padx=120)
    username_doc_entry = Entry(optionsFrame, width=30,textvariable=send_doc_user_var)
    username_doc_entry.insert(0, "User Name")
    username_doc_entry.grid(row=4, column=1, padx=30)
    username_doc_entry.bind("<Button-1>", lambda event: clear_entry(event, username_doc_entry))
    username_doc_btn = Button(optionsFrame, text="Select doc", command=send_docs)
    username_doc_btn.grid(row=5, column=1, padx=30, pady=15)

    # Change Profile_pic
    my_prof_pic_Label = Label(optionsFrame, text="select new profile")
    my_prof_pic_Label.grid(row=6, column=0, padx=30)
    my_prof_pic_btn = Button(optionsFrame, text="Select Image", command=change_profile)
    my_prof_pic_btn.grid(row=7, column=0, padx=30, pady=15)

    # New Message_info
    new_msgs_infoLabel = Label(optionsFrame, text="New Messages details")
    new_msgs_infoLabel.grid(row=6, column=1, padx=30)
    new_msgs_infobtn = Button(optionsFrame, text="Check New Messages", command=check_msgs)
    new_msgs_infobtn.grid(row=7, column=1, padx=30, pady=15)

    # Send Message
    userLabel = Label(optionsFrame, text="Enter user to Send message")
    userLabel.grid(row=8, column=0, padx=30,pady=10)
    user_entry = Entry(optionsFrame, width=30,textvariable=send_msg_user_var)
    user_entry.insert(0, "User Name")
    user_entry.grid(row=9, column=0, padx=30)
    user_entry.bind("<Button-1>", lambda event: clear_entry(event, user_entry))

    send_msg_user_entry = Entry(optionsFrame, width=30,textvariable=send_msg_var)
    send_msg_user_entry.insert(0, "Write message")
    send_msg_user_entry.grid(row=10, column=0, padx=30)
    send_msg_user_entry.bind("<Button-1>", lambda event: clear_entry(event, send_msg_user_entry))
    send_msg_user_btn = Button(optionsFrame, text="Send message", command=send_msg)
    send_msg_user_btn.grid(row=11, column=0, padx=30, pady=2)

    # Get User Details
    get_user_detailsLabel = Label(optionsFrame, text="Enter user to get Details")
    get_user_detailsLabel.grid(row=8, column=1, padx=30,pady=10)
    get_user_details_entry = Entry(optionsFrame, width=30,textvariable=user_details_var)
    get_user_details_entry.insert(0, "User Name")
    get_user_details_entry.grid(row=9, column=1, padx=30)
    get_user_details_entry.bind("<Button-1>", lambda event: clear_entry(event, get_user_details_entry))
    get_user_details_btn = Button(optionsFrame, text="Get Details", command=user_details)
    get_user_details_btn.grid(row=10, column=1, padx=30, pady=10)



    window_screen.mainloop()