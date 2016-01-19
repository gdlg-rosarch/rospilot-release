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
#ifndef ROSPILOT_BACKGROUND_IMAGE_SINK_H
#define ROSPILOT_BACKGROUND_IMAGE_SINK_H

#include<future>
#include<mutex>

#include<transcoders.h>
#include<resizer.h>
#include<image_sink.h>
#include<sensor_msgs/CompressedImage.h>

namespace rospilot {

class BackgroundImageSink 
{
private:
    ImageSink * sink;
    H264Encoder * encoder;
    Resizer * resizer;
    std::future<void> sinkFuture;
    std::mutex lock;
    bool closed = false;
    sensor_msgs::CompressedImage currentFrame;

public:
    // encoder may be null to indicate that no encoding is needed
    // NOTE: imageSink will not be released
    BackgroundImageSink(ImageSink *imageSink, H264Encoder *h264Encoder, Resizer *resizer);

    // thread-safe
    void addFrame(sensor_msgs::CompressedImage const *image);

    ~BackgroundImageSink();
};

}

#endif
