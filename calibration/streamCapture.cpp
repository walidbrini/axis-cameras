#include <iostream>
#include <unistd.h>
#include <fstream>

#include <opencv2/opencv.hpp>
#include <nlohmann/json.hpp>

using namespace cv;
using namespace std;
using json = nlohmann::json;

string build_rtsp_url(const json& cfg)
{
    string user = cfg.value("username", "");
    string pass = cfg.value("password", "");
    string ip   = cfg.value("camera_ip", "");
    string path = cfg.value("path", "/axis-media/media.amp");

    return "rtsp://" + user + ":" + pass + "@" + ip + path;
}

int main()
{
    // -------------------------
    // Load config
    // -------------------------
    ifstream file("../config/camera.json");

    if (!file)
    {
        cerr << "Failed to open config file" << endl;
        return -1;
    }

    json config;
    file >> config;

    string RTSP_URL = build_rtsp_url(config);

    cout << "RTSP URL: " << RTSP_URL << endl;

    // -------------------------
    // Video capture
    // -------------------------
    VideoCapture capture;

    while (true)
    {
        if (!capture.isOpened())
        {
            cout << "Connecting..." << endl;

            capture.open(RTSP_URL, cv::CAP_FFMPEG);

            if (!capture.isOpened())
            {
                cout << "Connection failed. Retrying in 5 seconds..." << endl;
                sleep(5);
                continue;
            }

            cout << "Connected." << endl;
        }

        Mat frame;

        if (!capture.read(frame))
        {
            cout << "Stream lost. Reconnecting..." << endl;

            capture.release();
            sleep(5);
            continue;
        }

        imshow("RTSP Stream", frame);

        if (waitKey(1) == 'q')
            break;
    }

    capture.release();
    destroyAllWindows();

    return 0;
}