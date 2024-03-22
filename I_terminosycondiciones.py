"""
Giulio Dominini
Microbits
El iman

"""
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

floatlayout = FloatLayout()
floatlayout.add_widget(Label(
    text="Terms and Conditions",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='30sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .90}
))

terminos_condiciones = TextInput(
	text="""BY INSTALLING, COPYING OR OTHERWISE USING THE SOFTWARE YOU ARE DEEMED TO AGREE TO THE TERMS AND CONDITIONS OF THIS DOCUMENT. 
    	AGREE TO THE TERMS AND CONDITIONS OF THIS DOCUMENT.
		The user acquires only the right to use it freely on his computer system, with the only limitations detailed below in this document:
		In no case this license implies the cession of the right of property on the software, reason why the user will not be able to proceed to its redistribution, sale, or modification of the internal code of the program by means of inverse engineering or by any other procedure, without the express authorization and in writing of the author.
		The license is exclusive and non transferable to third parties, is indefinite in time, and gives the right to install the program on a single computer, or on a single group of computers interconnected together in a local area network and necessarily sharing user data when the version offered provides this function.
		Installation of the Software on another computer or another local network is always possible on condition that the complete uninstallation process is followed, starting from the Windows control panel, section "Add/Remove Programs", on the computer or network computers where it was previously installed, and then physically removing all program files from the disk.
		The license is effective until cancelled. Cancellation will occur automatically without notice from Microbits if any of the conditions set forth in this license are not met.  In no case will any refund of amounts paid be made when the serial number has been issued.  In order to avoid misunderstandings, Microbits offers the possibility to test the software before requesting the serial number.
		Microbits guarantees the proper functioning of the offered system.
		In view of the material impossibility of testing the program on the great variety of existing computers, with all operating systems and their different versions and updates in circulation, and in interaction with the many individual and local network configurations that can be found in practice, Microbits considers that it is the user himself who  in any case must make sure beforehand, by use or thorough testing prior to purchase, of the complete suitability of the software to the specific circumstances of his computer equipment, his network, and his company, and that, in an affirmative assumption, the customer accepts the program as is, without the right to demand any type of modification that has not been previously agreed upon.
		REGISTRATION DATA FOR THE ISSUANCE OF AN AUTHORIZATION LICENSE
		Microbits will request registration data in order to issue the software's Definitive Enabling License.  It is the USER'S EXCLUSIVE RESPONSIBILITY to inform commercial data corresponding to his/her activity, taking into account that certain data such as telephone, e-mail or company name may be automatically assigned in reports or tax receipts.   The registration data sent to request the serial number of qualification CANNOT BE MODIFIED in case of errors or omissions once the serial has been issued, reason why the User must pay special attention before sending it.  For CORRECTIONS SUBSEQUENT TO THE ISSUANCE OF THE USER LICENSE, the User will have to pay again for the same one since a new license will be generated.
		LIABILITY FOR FAILURES
		In case the application contains any error, Microbits undertakes to resolve it as soon as possible, but shall not be liable for any direct or indirect damage resulting from the use or inability to use the application, including the loss of data that may occur on the occasion of, or in connection with, the use of the authorized software.   The possibility offered to the User to TEST BEFORE PURCHASE, minimizes the risks of encountering faults that could complicate the implementation.
		RESPONSIBILITY FOR THE DATA
		The integrity and preservation of the data files is the sole responsibility of the user, who must obtain and maintain a backup copy at least once a day.  To facilitate the realization of backup copies, the software centralizes all the data in a single folder.
		The User shall keep the e-mail received with the software serial number for backup purposes, in case of breakage or equipment change, in case the software needs to be reinstalled.
		Microbits will keep the data safe for one calendar year and may be requested by sending an email "exclusively" from the registered email address.   Any request sent from an email address other than the registered email address will be rejected.
		In the event that the resubmission of registration data is requested, after the calendar year has elapsed, a new license fee must be paid in order to obtain it.
		SCOPE OF MICROBIT LIABILITY
		Microbits' liability shall be limited to the replacement of the defective program or, at most, the implementation of a new version free of charge, always within 30 days from the date of purchase. This limited warranty is void if the software defect is the result of accident, abuse or misuse.
		USER'S RIGHT TO TRY BEFORE YOU BUY
		For greater security about the application, the User has the possibility to download the software in DEMO mode without having to pay anything for this service. Microbits recommends that the User makes use of this right, to avoid misunderstandings and make the purchase being fully secure.
		REFUNDS DUE TO USER DISSATISFACTION
		Counting the User with the possibility to TRY BEFORE BUYING and to make all the consultations that he deems necessary, it is considered unfeasible the possibility of money refunds due to disagreement, interpretation errors or for diverse reasons that lead the User not to use the application. Under no circumstances money refunds will be made for Licenses paid when the serial number of qualification has been issued.
		In those cases where a refund is requested for Paid Purchases without the serial number of authorization having been issued, refunds will be generated within 60 days of the request for an amount equivalent to the amount of the purchase minus 20% (twenty percent) in concept of payment gateway expenses.
		AFTER-SALES TECHNICAL SUPPORT
		The User Support will be made by entering the exclusive area of CUSTOMERS, for which the User must register in the site to obtain his User and Password of access. 
		The answers to Support Tickets will be answered according to your Support plan, within 48 working hours, 24 working hours or 24 hours (working or not).
		PERSONALIZED ATTENTION
		The attention to Users for QUESTIONS prior to the purchase, can be made by e-mail (ovandogiulio.00@gmail.com) from Monday to Friday from 9:00 to 12:00 Hs.  Microbits offers telephone communication at 351-6966161.
		The Email inquiries that do not involve technical assistance will be answered only when time permits during business hours.  Queries related to technical assistance will be referred to the


		""",
    size_hint=(.90, .79),
    multiline=True,
    pos_hint={'x': .05, 'y': .13},
    readonly= True

)


floatlayout.add_widget(Label(
    text="Accept Terms and Conditions:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='25sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0.05, 'y': .05}
))




desp_fix = CheckBox(
    size_hint=(0.27, .04),
    color=(1, 1, 1, 1),
    pos_hint={'x': .35, 'y': .08}
)



btn_siguiente = Button(
    text="Next",
    size_hint=(0.15, .05),
    background_color=(0, 0, 0, 1),
    font_size='25sp',
    pos_hint={'x': .85, 'y': .03}
)



floatlayout.add_widget(terminos_condiciones)
floatlayout.add_widget(desp_fix)

floatlayout.add_widget(btn_siguiente)