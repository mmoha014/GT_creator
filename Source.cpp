#include <opencv2/opencv.hpp>
#include <opencv2/tracking.hpp>
#include <opencv2/core/ocl.hpp>

using namespace cv;
using namespace std;

struct Rep
{
	int topF;
	vector<int> bottomF; 
	float uVelocity, dVelocity;
	int distance;
	float uROM, dROM; 
	double duration, liftT, lowT;
	Point3f top;
	vector<Point3f> bottom;

	Rep rep()
	{
		this->topF = 0;
		this->distance = 0;
		this->uROM = 0.0; 
		this->dROM = 0.0; 
		this->duration = 0.0;
		this->liftT = 0.0; 
		this->lowT = 0.0;
		this->top.x = 0;
		this->top.y = 0; 
		this->uVelocity = 0.0;
		this->dVelocity = 0.0;
	}

	Rep rep(int time, int mT, int far, double dur, double loT, double liT, float tx, float ty, float v, float dv)
	{
		this->topF = time;
		this->distance = far;
		this->duration = dur;
		this->liftT = liT;
		this->lowT = loT; 
		this->top.x = tx;
		this->top.y = ty;
		this->uVelocity = v;
		this->dVelocity = dv;
	}

	~Rep()
	{
		this->topF = 0;
		this->distance = 0;
		this->uROM = 0.0;
		this->dROM = 0.0;
		this->duration = 0.0;
		this->liftT = 0.0;
		this->lowT = 0.0; 
		this->top.x = 0;
		this->top.y = 0;
		this->uVelocity = 0.0;
		this->dVelocity = 0.0;
	}

};

ofstream gtFile;
ofstream rFile; 
string videoId = "D7"; 
vector<Rep> GT_reps;
int gtCount = 0;
int frameCount = 0; 
Rep* gt_rep = new Rep();

Point b1rW, b1rE, b1rS, trW, trE, trS, b2rW, b2rE, b2rS;

int tF = 0;
int stF = 0;
int eF = 0;

static void onMouse(int event, int x, int y, int, void*)
{

	if (event != EVENT_LBUTTONDOWN)
		return;

	Point seed = Point(x, y);

	gtCount++;

	if (gtCount == 1)
	{
		gtFile.open("GT_" + videoId + ".txt");
		b1rW = seed; 
		stF = frameCount;
		cout << "Start frame: " << stF << endl;
		cout << "b1 Right Wrist (x,y):		(" << b1rW.x << "," << b1rW.y << ")" << endl;
	}

	if (gtCount == 2)
	{
		b1rE = seed;
		cout << "b1 Right Elbow (x,y):		(" << b1rE.x << "," << b1rE.y << ")" << endl; 
	}

	if (gtCount == 3)
	{
		b1rS = seed;
		cout << "b1 Right Shoulder(x,y):		(" << b1rS.x << "," << b1rS.y << ")" << endl;
	}

	if (gtCount == 4)
	{
		tF = frameCount; 
		trW = seed;
		cout << "Top frame: " << tF << endl;
		cout << "t Right Wrist (x,y):		(" << trW.x << "," << trW.y << ")" << endl;

	}

	if (gtCount == 5)
	{
		trE = seed;
		cout << "t Right Elbow (x,y):		(" << trE.x << "," << trE.y << ")" << endl;
	}

	if (gtCount == 6)
	{
		trS = seed;
		cout << "t Right Shoulder(x,y):		(" << trS.x << "," << trS.y << ")" << endl;
	}

	if (gtCount == 7)
	{
		eF = frameCount;
		b2rW = seed;
		cout << "End frame: " << eF << endl;
		cout << "b2 Right Wrist (x,y):		(" << b2rW.x << "," << b2rW.y << ")" << endl;

	}

	if (gtCount == 8)
	{
		b2rE = seed;
		cout << "b2 Right Elbow (x,y):		(" << b2rE.x << "," << b2rE.y << ")" << endl;
	}

	if (gtCount == 9)
	{
		b2rS = seed;
		cout << "b2 Right Shoulder(x,y):		(" << b2rS.x << "," << b2rS.y << ")" << endl;

		GT_reps.push_back(*gt_rep); 

		gtFile << GT_reps.size() << " " << stF << " " << tF << " " << eF << " " 
								<< b1rW.x << " " << b1rW.y << " " << b1rE.x << " " << b1rE.y << " " << b1rS.x << " " << b1rS.y << " " 
								<< trW.x << " " << trW.y << " " << trE.x << " " << trE.y << " " << trS.x << " " << trS.y << " "
								<< b2rW.x << " " << b2rW.y << " " << b2rE.x << " " << b2rE.y << " " << b2rS.x << " " << b2rS.y << endl; 

		cout << GT_reps.size() << " " << stF << " " << tF << " " << eF << " "
								<< b1rW.x << " " << b1rW.y << " " << b1rE.x << " " << b1rE.y << " " << b1rS.x << " " << b1rS.y << " "
								<< trW.x << " " << trW.y << " " << trE.x << " " << trE.y << " " << trS.x << " " << trS.y << " "
								<< b2rW.x << " " << b2rW.y << " " << b2rE.x << " " << b2rE.y << " " << b2rS.x << " " << b2rS.y << endl;
		

		gt_rep = new Rep();
		
		stF = frameCount;

		b1rW = Point();
		b1rE = Point();
		b1rS = Point();

		b1rW = b2rW;
		b1rE = b2rE;
		b1rS = b2rS;

		gtCount = 3; 

	}
}

void calcDiff(); 

int main(int argc, char **argv)
{

	//calcDiff();
	// Read video
	VideoCapture video(videoId + ".mp4");
	//VideoCapture video(0); 
	
	// Exit if video is not opened
	if (!video.isOpened())
	{
		cout << "Could not read video file" << endl;
		return 1;
	}

	// Read first frame 
	Mat frame, temp2;
	bool ok = video.read(frame);
	
	
	namedWindow("Frame", WINDOW_AUTOSIZE); 

	while (video.read(frame))
	{
		frameCount++; 
			
		resize(frame, frame, Size(1000, 640));

		transpose(frame, frame);
		rotate(frame, frame, ROTATE_90_CLOCKWISE);

		flip(frame, frame, +1);

		cin.get(); 

		setMouseCallback("Frame", onMouse, 0);

		// Display frame.
		imshow("Frame", frame);

		// Exit if ESC pressed.
		int k = waitKey(1);
		if (k == 27)
		{
			break;
		}

	}

	gtFile.close();
	rFile.close(); 

	cout << "Finished" << endl;

	return 0; 
}

void calcDiff()
{
	ifstream rFile; 
	ifstream gtFile;
	ofstream roFile, goFile; 
	Rep gtRep; 
	Rep prRep; 
	vector<Rep> gtReps;
	vector<Rep> prReps;

	int TP = 0; 
	int FP = 0; 
	 
	rFile.open("out_" + videoId + ".txt");
	gtFile.open(videoId + ".txt");
	//roFile.open(videoId + "ROM.txt");
	//goFile.open(videoId + "gtROM.txt");

	
	if (rFile.is_open() && gtFile.is_open())
	{
		cout << "Opened Files ... " << endl << endl; 
		cout << "Generating Stats... " << endl; 
	}
	else
	{
		cout << "Error Reading Files" << endl;
	}

	while (rFile)
	{

		cout << "READING REP FILE" << endl; 

		int num;
		int bF, bF1;
		float bFx, bFy; 
		Point3f *bFp, *bFp1;
		int tx, ty; 
		float bF1x, bF1y; 

		bFp = new Point3f(); 
		bFp1 = new Point3f(); 

		rFile >> num >> bF >> prRep.topF >> bF1 >> bFp->x >> bFp->y >> prRep.top.x >> prRep.top.y >> bFp1->x >> bFp1->y;

		prRep.bottomF.push_back(bF);
		prRep.bottomF.push_back(bF1);
		prRep.bottom.push_back(*bFp);
		prRep.bottom.push_back(*bFp1); 

		prRep.uROM = abs(prRep.top.y - prRep.bottom[0].y);
		prRep.dROM = abs(prRep.top.y - prRep.bottom[1].y);
		prRep.distance = (abs(prRep.bottom[0].y - prRep.top.y) + abs(prRep.bottom[1].y - prRep.top.y));
		
		prRep.liftT = (abs(prRep.bottomF[0] - prRep.topF) / 30.0);
		prRep.lowT = (abs(prRep.bottomF[1] - prRep.topF) / 30.0);
		
		prRep.uVelocity = ((abs(prRep.top.y - (prRep.bottom[0].y))) / prRep.liftT);
		prRep.dVelocity = ((abs(prRep.top.y - (prRep.bottom[1].y))) / prRep.lowT);

		//roFile << prRep.distance << endl;

		if (prReps.empty())
			prReps.push_back(prRep);
		if (!prReps.empty() && bF != prReps[prReps.size() - 1].bottomF[0])
			prReps.push_back(prRep); 

		cout << num << " " << bF << " " << prRep.topF << " " << bF1 << " " << bFp->x << " " << bFp->y << " " << prRep.top.x << " " << prRep.top.y << " " << bFp1->x << " " << bFp1->y << endl;

		prRep.bottomF.clear();

		delete bFp; 
		delete bFp1;

	}

	//roFile.close();

	while (gtFile)
	{

		cout << "READING GT FILE" << endl;

		int num;
		int bF, bF1;
		float bFx, bFy;
		Point3f *bFp, *bFp1;
		int tx, ty;
		float bF1x, bF1y;

		bFp = new Point3f();
		bFp1 = new Point3f();

		gtFile >> num >> bF >> gtRep.topF >> bF1 >> bFp->x >> bFp->y >> gtRep.top.x >> gtRep.top.y >> bFp1->x >> bFp1->y;
		gtRep.bottomF.push_back(bF);
		gtRep.bottomF.push_back(bF1);
		gtRep.bottom.push_back(*bFp);
		gtRep.bottom.push_back(*bFp1);

		gtRep.uROM = abs(gtRep.top.y - gtRep.bottom[0].y); 
		gtRep.dROM = abs(gtRep.top.y - gtRep.bottom[1].y);
		gtRep.distance = (abs(gtRep.bottom[0].y - gtRep.top.y) + abs(gtRep.bottom[1].y - gtRep.top.y));
		
		gtRep.liftT = (abs(gtRep.bottomF[0] - gtRep.topF) / 30.0);
		gtRep.lowT = (abs(gtRep.bottomF[1] - gtRep.topF) / 30.0);
		
		gtRep.uVelocity = ((abs(gtRep.top.y - (gtRep.bottom[0].y))) / gtRep.liftT);
		gtRep.dVelocity = ((abs(gtRep.top.y - (gtRep.bottom[1].y))) / gtRep.lowT);

		//goFile << gtRep.distance << endl; 

		if (gtReps.empty())
			gtReps.push_back(gtRep);
		if (!gtReps.empty() && bF != gtReps[gtReps.size() - 1].bottomF[0])
			gtReps.push_back(gtRep);

		cout << num << " " << bF << " " << gtRep.topF << " " << bF1 << " " << bFp->x << " " << bFp->y << " " << gtRep.top.x << " " << gtRep.top.y << " " << bFp1->x << " " << bFp1->y << endl;

		gtRep.bottomF.clear();

		delete bFp;
		delete bFp1;

	}

	//goFile.close(); 

	int repCount = 0; 

	float liROM_error = 0.0; 
	float loROM_error = 0.0; 
	double liT_error = 0; 
	double loT_error = 0;
	double liV_error = 0.0;
	double loV_error = 0.0;

	ofstream reFile, teFile, veFile;
	reFile.open(videoId + "RE.txt");
	teFile.open(videoId + "TE.txt");
	veFile.open(videoId + "VE.txt"); 

	for (Rep r : prReps)
	{

		repCount++; 

		for (Rep g : gtReps)
		{

			cout << "Rep: " << repCount << endl;

			if (abs(r.bottomF[0] - g.bottomF[0]) <= 15)
			{
				cout << repCount << endl; 
				
				liROM_error = (abs(r.uROM - g.uROM));
				loROM_error = (abs(r.dROM - g.dROM));
				liT_error = (abs(r.liftT - g.liftT));
				loT_error = (abs(r.lowT - g.lowT)); 
				liV_error = (abs(r.uVelocity - g.uVelocity)); 
				loV_error = (abs(r.dVelocity - g.dVelocity)); 

				reFile << liROM_error << " " << loROM_error << endl; 

				teFile << liT_error << " " << loT_error << endl;

				veFile << liV_error << " " << loV_error << endl;

								
			}
		}
	}


	reFile.close(); 
	teFile.close();
	veFile.close(); 
	rFile.close();
	gtFile.close(); 

}

