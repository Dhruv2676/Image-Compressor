# Importing Necessary Modules For The Program To Use.
from PIL import Image
import os
import time
import re
import shutil
import statistics

class Compressor:
    def __init__(self):
        self.line_break = "\n------------------------------------------------------\n"

        self.source = ""
        self.destination = ""
        self.record_path = "Record.txt"
        self.png = {"index":None, "directories": ["C:/Users/DHRUV/Desktop/PNG/", "C:/Users/DHRUV/AppData/Local/PNG/"]}

        self.avg = {"original": [], "compressed": [], "percentage": []}

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

    def average_compression(self, status, original=0, compressed=0):
        if status == "append":
            self.avg["original"].append(original)
            self.avg["compressed"].append(compressed)
            self.avg["percentage"].append(int(((original - compressed)/original)*100))
        elif status == "sumup":
            if self.avg == []:
                return None

            per_image_avg = statistics.mean(self.avg["percentage"])
            total_avg = int((((sum(self.avg["original"]) - sum(self.avg["compressed"]))/sum(self.avg["original"]))*100))

            average = int((per_image_avg + total_avg)/2)
            return average

    def folder_creator(self, current_folder):
        if self.source == current_folder:
            return self.destination
        elif self.source in current_folder:
            extra = current_folder.replace(self.source, "")
            current_destination_path = self.destination + extra

            if not os.path.isdir(current_destination_path):
                os.mkdir(current_destination_path)
            return current_destination_path

        else:
            return

    def png_folder_operator(self, status):
        if status == "create":
            for index, directory in enumerate(self.png["directories"]):
                if not os.path.isdir(directory):
                    self.png["index"] = index
                    os.mkdir(directory)
                return True
        if status == "delete":
            shutil.rmtree(self.png["directories"][self.png["index"]], ignore_errors=True)
            return True

    def png_compressor(self, path, image, destination):
        if self.png["index"] == None:
            self.png_folder_operator(status="create")

        jpg_image = image[:-4] + ".jpg"

        picture_png = Image.open(path + "/" + image, "r") # Opens The .png File.
        picture = picture_png.convert('RGB') # Converts The .png File To .jpg File But It Is Saved In Memory.
        picture.save(self.png["directories"][self.png["index"]] + "/" + jpg_image) # Saves It On The Hard Disk In The Source Directory.

        picture = Image.open(self.png["directories"][self.png["index"]] + "/" + jpg_image, "r")
        picture.save(destination + "/" + jpg_image, optimize=True, quality=30)

        self.record(image) # Record The Image Through A Function Defined Later.

        org_size = int(os.path.getsize(path + "/" + image) / 1024)
        compressed_size = int(os.path.getsize(destination + "/" + jpg_image) / 1024)

        print("{: <75}{: >20}{: >20}".format(image, str(org_size) + " KB", str(compressed_size) + " KB")) # Prints The Name Of The File And The Size After Compression In 2 Neat Columns.
        self.average_compression(status="append", original=org_size, compressed=compressed_size)

    def compress(self, recorded_files):
        for path, folders, files in os.walk(self.source):
            current_dest = self.folder_creator(path)

            for image in files:
                if image.endswith(".jpg") or image.endswith(".JPG") or image.endswith(".jpeg"):
                    if image + "\n" not in recorded_files:
                        picture = Image.open(path + "/" + image, "r")
                        picture.save(current_dest + "/" + image, optimize=True, quality=30)

                        self.record(image) # Record The Image Through A Function Defined Later.

                        org_size = int(os.path.getsize(path + "/" + image) / 1024)
                        compressed_size = int(os.path.getsize(current_dest + "/" + image) / 1024)

                        print("{: <75}{: >20}{: >20}".format(image, str(org_size) + " KB", str(compressed_size) + " KB")) # Prints The Name Of The File And The Size After Compression In 2 Neat Columns.
                        self.average_compression(status="append", original=org_size, compressed=compressed_size)

                elif image.endswith(".png"):
                    if image + "\n" not in recorded_files:
                        self.png_compressor(path, image, current_dest)

                else: # If The Image Is Not A .jpg or .jpeg File Then It Continues Through The Loop.
                    continue

    def main(self):
        self.source = input("Enter The Directory Path Where The Images Are Located: ") # This Is The Directory From Which The Images Will Be Compressed. Change This According To Your Needs.
        self.destination = input("Enter The Directory Path Where The Compressed Images Are To Be Saved: ") # This Is The Directory Where All The Compressed Images Be Saved. Change This According To Your Needs.
        print("\n")
        self.ideal_path()

        self.clear_record()

        recorded_files = self.read_record()

        print("{: <75}{: >20}{: >20}".format("Name", "Original Size", "Compressed Size")) # Prints The Heading Of The Columns.
        time.sleep(1)
        self.compress(recorded_files)

        try:
            avg = self.average_compression(status="sumup")
        except:
            pass
        
        if avg == None:
            print("We Didn't Find Any Images To Compress In The Source Directory!")
            quit()

        if self.png["index"] != None:
            self.png_folder_operator(status="delete")

        print(f"\nThe Compression Rate Throughout Was {avg}%\n")

        print(f"Done. All Images In \"{self.destination}\"")

Compressor = Compressor()
Compressor.main()