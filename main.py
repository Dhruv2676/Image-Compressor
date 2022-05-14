# Importing Necessary Modules For The Program To Use.
from PIL import Image
import os
import re
import shutil
import statistics

class Compressor:
    def __init__(self):
        self.line_break = "\n-------------------------------------------------------------\n"

        self.source = ""
        self.destination = ""
        self.record_path = "Record.txt"

        self.avg = []

    def ideal_path(self):
        """
        This Function Tries To Eliminate Any Possibilities Of Any Error Caused By The Path Provided By The User Or Hard-Coded Paths By The Developer.
        """
        if not os.path.exists(self.source): # Checks If The Source Directory Exists Else Prints An Error Message For The User.
            print(f"\nThe Folder {self.source} Doesn't Exist. Please Create The Folder And Provide The Path To It Seeing The README.md File - \"#File Path Syntax\". \n")
            quit()
        
        if not os.path.exists(self.destination): # Checks If The Destination Directory Exists Else Prints An Error Message For The User.
            print(f"\nThe Folder {self.destination} Doesn't Exist. Please Create The Folder And Provide The Path To It Seeing The README.md File - \"#File Path Syntax\". \n")
            quit()

        if not os.path.isfile(self.record_path): # Checks If The Record Text File Exists Else Prints An Error Message For The User.
            print(f"\nThe Record Text File Path -- {self.record_path} Doesn't Exist. Please Check Section \"#File Path Syntax\" In README.md File For More Information. \n")
            quit()

    def clear_record(self):
        """
        This Function Asks The User If She/He Wants To Clear The Record Text File. If Yes, Then Clears It. If No, Then It Doesn't Anything.
        Then Asks The User If He Wants To Run The Rest Of The Program. If Yes, Then Continues With The Rest, Else Quits The Program.
        """
        if input("Do You Want To Clear Records? [y/n] : ").lower() == "y": # Asks For Input And Checks If It Is "y".
            with open(self.record_path, "w"): # If "y" Then Clears The Record.
                pass
        print(self.line_break)
        if input("Do You Want To Run The Program? [y/n] : ").lower() == "n": # Then Asks For Running The Program.
            quit() # If Yes, Quits The Program.
        print(self.line_break)

    def record(self, image):
        """
        This Function Recieves The Name Of The Image Being Compressed, Then Writes The Name In A .txt File Whose Path Is Recieved When Creating
        An Instance Of The Class. One Image File Name Is On One Line in .txt File.
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

    def average_compression(self, status, original=0, compressed=0):
        if status == "append":
            self.avg.append(int(((original - compressed)/original)*100))
        elif status == "sumup":
            if self.avg == []:
                return None

            per_image_avg = statistics.mean(self.avg)
            return per_image_avg

    def png_compressor(self, image):
        jpg_image = image[:-4] + ".jpg"
        print(jpg_image)

        picture_png = Image.open(self.source + "/" + image, "r") # Opens The .png File.
        picture = picture_png.convert('RGB') # Converts The .png File To .jpg File But It Is Saved In Memory.
        picture.save(self.destination + "/" + jpg_image, optimize=True, quality=30) # Saves It On The Hard Disk In The Source Directory.

        #picture = Image.open(self.png["directories"][self.png["index"]] + jpg_image, "r")
        #picture.save(self.destination + "/" + jpg_image, optimize=True, quality=30)

        self.record(image) # Record The Image Through A Function Defined Later.

        org_size = int(os.path.getsize(self.source + "/" + image) / 1024)
        compressed_size = int(os.path.getsize(self.destination + "/" + jpg_image) / 1024)

        print("{: <75}{: >20}{: >20}".format(image, str(org_size) + " KB", str(compressed_size) + " KB")) # Prints The Name Of The File And The Size After Compression In 2 Neat Columns.
        self.average_compression(status="append", original=org_size, compressed=compressed_size)

    def compress(self, recorded_files):
        for image in os.listdir(self.source):
            if image.endswith(".jpg") or image.endswith(".JPG") or image.endswith(".jpeg"):
                if image + "\n" not in recorded_files:
                    picture = Image.open(self.source + "/" + image, "r")
                    picture.save(self.destination + "/" + image, optimize=True, quality=30)

                    self.record(image) # Record The Image Through A Function Defined Earlier.

                    org_size = int(os.path.getsize(self.source + "/" + image) / 1024)
                    compressed_size = int(os.path.getsize(self.destination + "/" + image) / 1024)

                    print("{: <75}{: >20}{: >20}".format(image, str(org_size) + " KB", str(compressed_size) + " KB")) # Prints The Name Of The File And The Size After Compression In 3 Neat Columns.
                    self.average_compression(status="append", original=org_size, compressed=compressed_size)

            elif image.endswith(".png"):
                if image + "\n" not in recorded_files:
                    self.png_compressor(image)

            else: # If The Image Is Not A .jpg or .jpeg File Then It Continues Through The Loop.
                continue

    def main(self):
        self.source = input("Enter The Directory Path Where The Images Are Located: ") # This Is The Directory From Which The Images Will Be Compressed. Change This According To Your Needs.
        self.destination = input("Enter The Directory Path Where The Compressed Images Are To Be Saved: ") # This Is The Directory Where All The Compressed Images Be Saved. Change This According To Your Needs.
        print(self.line_break)

        self.ideal_path()
        self.clear_record()

        recorded_files = self.read_record()

        print("{: <75}{: >20}{: >20}".format("Name", "Original Size", "Compressed Size")) # Prints The Heading Of The Columns.

        self.compress(recorded_files)

        try:
            average = self.average_compression(status="sumup")
        except:
            average = None
        
        if average == None:
            print("We Didn't Find Any Images To Compress In The Source Directory!")
            quit()

        print(self.line_break)
        print(f"\nThe Compression Rate Throughout Was {average}%\n")

        print(self.line_break)

        print(f"Done. All Images In \"{self.destination}\"")
        print(self.line_break)

Compressor = Compressor()
Compressor.main()