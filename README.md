```
Title:        Image Compressor
Author:       Dhruv   
Date:         February, 2021
```

# Image-Compressor
Given a `Source` Directory, The Program Will Compress *All The Images* In The Directory and Subdirectories. It Can Convert Only **.png**, **.jpeg**, **.jpg** Images.

Images Will Get Compressed And Then Saved In The *Destination* Folder. The Quality Of The Compressed Image Will Be Only 30% That Of The Original, *But That Too Is Not Noticeable At All*.

# How To Use
- If You Are Running The Program For The First Time Then You Have To Install The Dependencies/Requirements For The Program. To Do That:
  - Open A Command Prompt/Terminal In The Current Directory.
  - Then Run The Command `pip install -r requirements.txt` In The Prompt/Terminal.
- After Starting The Program It Will Ask You To Enter The `Source` Directory, From Where All The Images Will Be Found. Please Check [The Folder Path Syntax](#folder-path-syntax) Before You Enter Anything.
- Next, It Will Ask You For The `Destination` Ditrectory, Where All The Compressed Images Will Be Saved. Please Check [The Folder Path Syntax](#folder-path-syntax) Before You Enter Anything.
- Next It Will Ask You If You Want To Clear The Records, For Which Please Check [Record File Use](#record).
- When It Started Compressing The Images, It Will Display Some Details - The Name Of The Image, Original Size, Compressed Size. For More Information On How It Will Compress It Please Check [Compress Details](#compress-details).
- When It Completes The Compressing, It Will Print The Avg Compression Rate Of All The Images Compressed With Also The Destination Folder Where All The Compressed Images Will Be Found.

# Folder Path Syntax:
- The Path You Provide For The Source Directory Should Be In The Format ***"C:/Users/....."*** With A Front Slash (***"/"***) And Not A Back Slash (***"\\"***). The End Of The Path Should Also Contain A Front Slash (**"/"**), (Ex: **"C:/Users/"**) Without Which Also You Would Get An Error.
- The Same Goes For The Destination Directory.
- If You Have Changed The List Containing PNG Directories, Then The Same Goes With It As Well.

# What To/Can Change
1. You Can Change The List Of *PNG Directories* In **Line 16**. It Should Follow [The Folder Path Syntax](#folder-path-syntax).
2. The Record File's Name In **Line 15**.
3. You *Can* Change The Compression Rate In **Lines 131 and 149** To Any Other **Integer**. **But This Can Have Serious Consequences Towards How The Program Compresses Your Images, It Is Advisable Not To Change.**

*Please Do Not Change Any Other Line Except The Above Mentioned Ones.*

# Record
- When The Program Is Compressing The Images, If Will Save The Name Of The Image's File Name, So That If By An Error/Problem, It Stops Compressing Images Then Also You Can Start Again From Where You Left It.
- For The Above To Work You Should Not Clear The Record When Asked At The Start Of Program.

- **It Is Advisable To Clear The Records If You Are Compressing A New Folder With Images.**

# Compress Details
- The Program *Creates* New Subolders In The *Destination* Folder According To The Subfolders Present In The *Source* Folder And Places The Compressed Images Accordingly In The Subfolders In The *Destination*