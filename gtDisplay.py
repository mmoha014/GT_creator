import math 
import argparse 
import cv2 as cv2 

class Rep: 
    def __init__(self):
        self.stF = 0
        self.tF = 0 
        self.eF = 0 
        self.b1rW = [0,0]
        self.b1rE = [0,0]
        self.b1rS = [0,0]
        self.trW = [0,0]
        self.trE = [0,0]
        self.trS = [0,0]
        self.b2rW = [0,0]
        self.b2rE = [0,0]
        self.b2rS = [0,0]


def main(): 
    '''Possible Arguments''' 
    parse = argparse.ArgumentParser() 

    parse.add_argument('--video_file', type=str, default='videos/D7.mp4', help='Path to the video file to apply the Ground Truth data to')
    parse.add_argument('--gt_file', type=str, default='GT_files/GT_D7.txt', help='Path to the Ground Truth file intended to be displayed')

    args = parse.parse_args() 

    '''Used Variables''' 
    Reps = [] 
    f = [] 
    cFrame = 0 

    '''Open the desired ground truth file''' 
    try: 
        vFile = open(args.gt_file, 'r+') 
        
        for file in vFile: 
            for w in file.split(): 
                f.append(w)

            gtRep = Rep() 
            print (f) 
            
            gtRep.stF = f[1]
            gtRep.tF = f[2]
            #print (gtRep.tF)
            gtRep.eF = f[3] 
            gtRep.b1rW = [f[4],f[5]]
            gtRep.b1rE = [f[6],f[7]]
            gtRep.b1rS = [f[8],f[9]]
            gtRep.trW = [f[10],f[11]]
            gtRep.trE = [f[12],f[13]]
            gtRep.trS = [f[14],f[15]]
            gtRep.b2rW = [f[16],f[17]]
            gtRep.b2rE = [f[18],f[19]]
            gtRep.b2rS = [f[20],f[21]]

            Reps.append(gtRep) 
            f = []

        try: 
            cap = cv2.VideoCapture(args.video_file)

            while True: 
                ret, frame = cap.read() 
                cFrame += 1

                frame = cv2.resize(frame, (1000,640), interpolation=cv2.INTER_AREA)
                cv2.transpose(frame, frame) 
                
                cv2.imshow("frame", frame)

                for r in Reps: 
                    if cFrame == int(r.stF): 
                        
                        frame = cv2.circle(frame, (int(r.b1rW[0]), int(r.b1rW[1])), 5, (255, 0, 0), 2) 
                        frame = cv2.circle(frame, (int(r.b1rE[0]), int(r.b1rE[1])), 5, (255, 0, 0), 2) 
                        frame = cv2.circle(frame, (int(r.b1rS[0]), int(r.b1rS[1])), 5, (255, 0, 0), 2) 
                        
                        cv2.imshow("out", frame)
                        
                        #input(" ... ")
                    if cFrame == int(r.tF): 
                        
                        frame = cv2.circle(frame, (int(r.trW[0]), int(r.trW[1])), 5, (255, 0, 0), 2) 
                        frame = cv2.circle(frame, (int(r.trE[0]), int(r.trE[1])), 5, (255, 0, 0), 2) 
                        frame = cv2.circle(frame, (int(r.trS[0]), int(r.trS[1])), 5, (255, 0, 0), 2) 
                        
                        cv2.imshow("out", frame)
                        
                        #input(" ... ")

                    if cFrame == int(r.eF): 
                        
                        frame = cv2.circle(frame, (int(r.b2rW[0]), int(r.b2rW[1])), 5, (255, 0, 0), 2) 
                        frame = cv2.circle(frame, (int(r.b2rE[0]), int(r.b2rE[1])), 5, (255, 0, 0), 2) 
                        frame = cv2.circle(frame, (int(r.b2rS[0]), int(r.b2rS[1])), 5, (255, 0, 0), 2) 
                        
                        cv2.imshow("out", frame)
                        
                        #input(" ... ")                

                    #print ("...")

                if cv2.waitKey(1) & 0xFF == ord('q'): 
                    break 

        except Exception as ex: 
            print(ex) 
    except Exception as ex: 
        print (ex)



if __name__ == "__main__":
    main () 

   