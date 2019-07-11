clear all;
close all;
thesis = Thesis();
thesis.saveFiguresPrompt();

%% Link Budget Calculations 

%% Constants
global c
c = 299792458;
mhz = 1e6;
ghz = 1e9;
hz_to_ghz = 1/ghz;
hz_to_mhz = 1/mhz;

%% Parameters

fMin = 4.5e6;%9.02e6;
fMax = 9.28e6;
heightTx=1.75; % Height of a typical person in meters
heightRx=1.75;
frequencies = [4.5*mhz, 9.15*mhz];

%% Calculations
distances = 0:10:10000;

f = figure(1);
hold on
title('Loss vs Distance')
xlabel('Distance (Metres)')
ylabel('Loss (dB)')
losses = zeros(length(frequencies),length(distances));
labels = cell(1,length(frequencies));
for i=1:length(frequencies)
    freq = frequencies(i);
%     breakPointDistance = 4*pi*heightTx*heightRx*freq/c
    labels(1,i)={strcat(num2str(freq*hz_to_mhz),' MHz')};
    losses(i,:)=freespaceLoss(freq,distances);
end
plot(distances,losses);
legend(labels,'Location','southeast')
hold off
thesis.saveFigure(f,"freespace-loss-vs-distance")

thesis.savedFigures

function [loss] = freespaceLoss(fc,distance)
    global c
    loss = 20*log10(fc)+20*log10(distance)+20*log10(4*pi/c);
end