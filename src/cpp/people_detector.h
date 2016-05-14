/*********************************************************************
 *
 * Copyright 2012 the original author or authors.
 * See the NOTICE file distributed with this work for additional
 * information regarding copyright ownership.
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *    http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 *********************************************************************/
#ifndef ROSPILOT_PEOPLE_DETECTOR_H
#define ROSPILOT_PEOPLE_DETECTOR_H

#include<opencv2/objdetect.hpp>
#include<ros/ros.h>
#include<sensor_msgs/CompressedImage.h>
#include<image_sink.h>

extern "C" {
#include <turbojpeg.h>
#include <libswscale/swscale.h>
}

namespace rospilot {

class PeopleDetector : public ImageSink
{
private:
    cv::HOGDescriptor hog;
    ros::Publisher *detectedPeopleTopic;
    tjhandle handle;
    SwsContext *context;
    int width;
    int height;


public:
    PeopleDetector(ros::Publisher *topic, int width, int height);

    // thread-safe
    void addFrame(sensor_msgs::CompressedImage *image, bool keyFrame) override;

    ~PeopleDetector();
};

}

#endif
