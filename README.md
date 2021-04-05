```
Title:        Image Compressor
Author:       Dhruv   
Date:         February, 2021
```

# Image-Compressor
This Program Takes A Directory's Path `source` And A Destination Path `destination` and Then Analyzes The *Source*'s Contents To Find Any Images. Images of Only Specific Types Are Available TO Compress Such As **.png**, **.jpeg**, **.jpg**.

**.jpeg** and **.jpg** Image Types Will Get Compressed And Then Saved In The *Destination*. The Quality Of The File Will Be Only 30% That Of The Original But That Too Is Not Noticeable At All.

**.png** Image Type Will First Get Converted To **.jpg** Image Type And Then Get Compressed And Saved To The *Destination*. Then The **.png** File Will Be Moved To A Folder Called `PNG's` On The Desktop Which Will Be Created Automatically By The Program.

This Program Also Takes The Path Of A Text File. This Is Used To Record The Files Being Converted So That You Can Resume Whenever You Want On A Large Folder Of Images.

# What Can You Change:
- # Compulsory To Change:
  **Some Of The Path's Are Hard-Coded According To A Windows Computer, If You Are Using Any Other OS, Then Please Change All The Path's In The Code Wherever Possible According To Your OS.** 

  ***Sorry For The inconvenience Caused.***

  1. **Line 165** In `"Image Compressor.py"` File. Change It With The Directory's Path Where The Images Which Are To Be Compressed Are Located.
  2. **Line 166** In `"Image Compressor.py"` File. Change It With The Directory's Path Where The Compressed Images Are To Be Stored.
- # Can Be Changed:
  **Change These Things Only If You Understand The Code**

  1. **Line 167** In `"Image Compressor.py"` File. Change It With The Path Of A Text File Where The Records Are To Be Stored.
  2. **Line 12** In `"Image Compressor.py"` File. Change It With The Directory's Path Where All The **.png** Image Type Files Are To Be Stored.
  3. **Line 56** In `"Image Compressor.py"` File. You Can Change The Quality Of The Converted Image. **(Beware!! This Will Change The Size Of The File But This Will Result In A Degraded Image Quality With Just A Few Numbers.)**
  4. The Print Statements Can Be Changed According To Your Needs.

# Folder Path Syntax:
**If You Get A Syntax Error While Running The Code, Or A Error Message Is Printed By The Program, Then Please Read The Below Points.**
- The Path You Provide For The Source Directory (**Line 165**) Should Be In The Format ***"C:/Users/....."*** With A Front Slash (***"/"***) And Not A Back Slash (***"\\"***). The End Of The Path Should Also Contain A Front Slash (**"/"**), Without Which Also You Would Get An Error.
- The Same Goes For The Destination Directory (**Line 166**) and The Path Of The Record Text File (**Line 167**)
- If You Have Changed The PNG Directory Then The Same Goes With It As Well.

# How To Use:
- If You Are Running The Program For The First Time Then You Have To Install The Dependencies/Requirements For The Program. To Do That:
  - Open A Command Prompt/Terminal In This Program's Directory.
  - Then Run The Command `pip install -r requirements.txt` In The Prompt/Terminal.

- It Will Ask You For A Username And Password. You Are To Enter Only This Or Else You Wouldn't Be Able To Use The Program:
  - Username: ***Dhruv_2676***
  - Password: ***My_Program***
- After Entering The Correct Information You Will Be Asked If You Want To Clear The Records. If You Want To Start From The First On A Directory Then Press `y` And Continue.
- Then It Will Ask You If You Want To Continue With The Program. If You Just Wanted To Clear The Records And Leave Then Press `n` Or Else Press `y` and Continue.
- After Pressing `y` On The Above Prompt The Program Will Start Running And Printing Some Information On The Screen About Which File It Is Converting And The Size Of The File After Getting Converted In Neat Columns.
- Then Atlast It Will Print `Done` With The Path Of The *Destination*.
