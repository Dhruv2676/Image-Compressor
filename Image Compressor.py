# Importing Necessary Modules For The Program To Use.
from PIL import Image
import os
import time
import re

class Converter:
    def __init__(self):
        # Necessary Parameters For Use.
        self.source = ""
        self.destination = ""
        self.png_directory = "C:/Users/DHRUV/Desktop/PNG's/"
        self.record_path = "Record.txt"

        self.avg = []

    def ideal_path(self):
        """
        This Function Tries To Eliminate Any Possibilities Of Any Error Caused By The Path Provided By The User Or Harc-Coded Path's By The Owner.
        """
        try: # Checks If The Source Directory Exists Else Prints A Message For The User According To The Error.
            os.listdir(self.source)
        except FileNotFoundError:
            print(f"\nThe Folder {self.source} Doesn't Exist. Please Create The Folder And Provide The Path To It Seeing The README.md File. \n")
            quit()
        except SyntaxError:
            print(f"\nThe Folder Path You Provided -- {self.source} Is Not Correct. Please Check Section \"#File Path Syntax\" In README.md File For More Information. \n")
            quit()
        
        try: # Checks If The Destination Directory Exists Else Prints A Message For The User According To The Error.
            os.listdir(self.destination)
        except FileNotFoundError:
            print(f"\nThe Folder {self.destination} Doesn't Exist. Please Create The Folder And Provide The Path To It Seeing The README.md File. \n")
            quit()
        except SyntaxError:
            print(f"\nThe Folder Path You Provided -- {self.destination} Is Not Correct. Please Check Section \"#File Path Syntax\" In README.md File For More Information. \n")
            quit()

        try: # Checks If The Record Text File Exists Else Prints A Message For The User According To The Error.
            with open(self.record_path, 'r'):
                pass
        except FileNotFoundError:
            print(f"\nThe Record Text File Path -- {self.record_path} Doesn't Exist. Please Check Section \"#File Path Syntax\" In README.md File For More Information. \n")
            quit()
        except SyntaxError:
            print(f"\nThe Record Text File Path -- {self.record_path} You Provided Is Not Correct. Please Check Section \"#File Path Syntax\" In README.md File For More Information. \n")
            quit()

    def compress(self, listdr_jpg, recorded_files):
        """
        This Function Takes A List Of File Names In The Source Directory And A List Of All Recorded Files As List. Then Compresses Each 
        Of The .jpg or .jpeg Files, Which Has Not Been Recorded, Into The Destination Directory.
        """
        for image in listdr_jpg: # Loops Through All The File Names In The Source Directory.
            if image.endswith(".jpg") or image.endswith(".JPG") or image.endswith(".jpeg"): # Checks If The File Is A .jpg or .jpeg File.
                if image + "\n" not in recorded_files: # Checks If The Image Is In Recorded Files Or Not. If It's Not There Then Runs The Code Block Below.
                    picture = Image.open(self.source + image, "r") # Opens The Image In Reading Mode.
                    picture.save(self.destination + image, optimize=True, quality=30) # Saves The Picture In A Lesser Quality Which Is Not Noticeable.

                    self.record(image) # Record The Image Through A Function Defined Later.

                    org_size = int(os.path.getsize(self.source + image) / 1024)
                    compressed_size = int(os.path.getsize(self.destination + image) / 1024)

                    print("{: <75}{: >20}{: >20}".format(image, str(org_size) + " KB", str(compressed_size) + " KB")) # Prints The Name Of The File And The Size After Compression In 2 Neat Columns.
                    self.average_compression(True, org_size, compressed_size)
                else: # If It's Recorded The It Will Continue Through The Loop.
                    continue
            else: # If The Image Is Not A .jpg or .jpeg File Then It Continues Through The Loop.
                continue
        

    def convert_png(self, listdr):
        """
        This Function Takes In A List Of All Files, Then Checks For For Any .png Files In That Folder, If There Then Converts It To A .jpg
        And Then Transfer's The .png File To A Directory On The Desktop ( If "self.png_directory" Is Not Changed).
        """
        status = 0
        for image in listdr: # Loops Through Every File Name In The Directory.
            if image.endswith(".png"): # Checks If The File Is A .png File.
                if status == 0:
                    try:
                        os.listdir(self.png_directory) # Checks If The PNG Directory Exists.
                        status = 1
                    except:
                        os.mkdir(self.png_directory) # If It Doesn't Exist Then Creates It.
                        status = 1

                picture_png = Image.open(self.source + image, "r") # Opens The .png File.
                picture = picture_png.convert('RGB') # Converts The .png File To .jpg File But It Is Saved In Memory.

                picture.save(self.source + image[:-4] + ".jpg") # Saves It On The Hard Disk In The Source Directory.
                os.rename(self.source + image, self.png_directory + image) # Transfer's The .png File To The PNG Directory.

    def record(self, image):
        """
        This Function Recieves The Name Of The Image Being Compressed, Then Writes The Name In A .txt File Whose Path Is Recieved When Creating
        An Instance Of The Class. One File Name Is On One Line.
        """
        with open(self.record_path, "a") as file_record: # Opens The Record Text File In Appending Mode.
            file_record.write(image + "\n") # Writes The Name Of The Image On A New Line.

    def read_record(self):
        """
        This Function Reads The Record File And Returns A List Of All The Image File Names In The .txt File.
        """
        with open(self.record_path, "r") as file_record: # Opens The Record Text File In Reading Mode.
            all_images = file_record.readlines() # Reads All The Lines Of The .txt File.
            return all_images # Returns The List.

    def average_compression(self, stat, org=0, compressed=0):
        if stat:
            compression_percent = int(((org - compressed) / org) * 100)
            self.avg.append(compression_percent)
        else:
            tot_avg = int(sum(self.avg) / len(self.avg))
            return tot_avg

    def clear_record(self):
        """
        This Function Asks The User If She/He Wants To Clear The Record Text File. If Yes, The Clears It. If No, Then Doesn't.
        Then Asks The User If He Wants To Run The Rest Of The Program. If Yes, Then Continues With The Rest, Else Quits The Program.
        """
        if input("Do You Want To Clear Records? [y/n] : ").lower() == "y": # Asks For Input And Checks If It Is "y".
            with open(self.record_path, "w"): # If "y" Then Clears The Record.
                pass
            if input("Record Cleared. Do You Want To Run The Program? [y/n] : ").lower() == "n": # Then Asks For Running The Program.
                quit() # If Yes, Quits The Program.
        print("\n")

    def main(self):
        """
        This Function Makes It All Work ;)
        """
        self.source = input("Enter The Directory Path Where The Images Are Located: ") # This Is The Directory From Which The Images Will Be Compressed. Change This According To Your Needs.
        self.destination = input("Enter The Directory Path Where The Compressed Images Are To Be Saved: ") # This Is The Directory Where All The Compressed Images Be Saved. Change This According To Your Needs.
        print("\n")
        self.ideal_path()

        self.clear_record() # Then Asks For Clearing The Record Text File.

        all_files_directory_with_png = os.listdir(self.source) # Lists All The Files In The Source Directory.
        all_recorded_files = self.read_record() # Reads All The File Names In The Record Text File.

        if len(all_files_directory_with_png) == 0: # Checks If The Source Directory Is Emptpy, In The Case Prints A Message And Quits.
            print(f"No Images Found In Source Directory - \"{self.source}\"") # Prints A Message And Quits.
            quit() # Quits The Program.

        self.convert_png(all_files_directory_with_png) # Tries To Convert Any .png Images In The Source Directory.

        all_files_directory= os.listdir(self.source) # Now Lists All The Files In The Source Directory This Time Without Any .png Files.
        print("{: <75}{: >20}{: >20}".format("Name", "Original Size", "Compressed Size")) # Prints The Heading Of The Columns.
        time.sleep(1) # This Makes The Computer Wait For 1 Second, So That The User Can See The Headings Of The Columns Before It Starts Printing The Details.
        self.compress(all_files_directory, all_recorded_files) # Compress All The Images.

        avg = self.average_compression(False)
        print(f"\nThe Compression Rate Throughout Was {avg}%\n")

        print(f"Done. All Images In \"{self.destination}\"") # Prints A Message That Compressing Is Done.
      
Converter = Converter()
Converter.main() # Calls The Main Function.