# .otf2-reader

This is a Python program which uses otf2 libraries to open/read the traces in an Open trace format file(.otf2)

Inputs- Path of the anchor file(traces.otf2)
Outputs - Plots of the traces and an Excel file


Code overview-

1. "otf2.reader.open($path to the anchor file)" gives all the events in the trace file.
2. A for loop is used to traverse in the events and extract the Metrics from the events
3. Depending on the MetricsInstance the metrics are segregated and appended to their respective lists.
4. These lists are then plotted and also exported as an excel file. 


The code varies from case to case depending on the number of metrics being traced, so should alter the code accordingly. i.e is the lists appending and plotting part of the code.


-------------------------------------------------------------------------------------------------------------------------------
The MetricInstance of a metric can be know by checking manually i.e open the trace file from the terminal using the command "otf2 -open -A trace.otf2 >log "


Part of the text file generated from the above command 

METRIC_CLASS                           0  Occurrence: SYNCHRONOUS_STRICT, Kind: CPU, 3 Members: "PAPI_L1_DCM" <0>, "PAPI_L2_DCM" <1>, "PAPI_L2_DCH" <2>
METRIC_CLASS                           1  Occurrence: ASYNCHRONOUS, Kind: ABSTRACT, 1 Member: "CPU_Freq2" <3>
METRIC_INSTANCE                        2  Class: 1, Recorder: "" <4294967296>, Scope: SYSTEM_TREE_NODE "tegra-ubuntu" <1>
METRIC_CLASS                           3  Occurrence: ASYNCHRONOUS, Kind: ABSTRACT, 1 Member: "CPU_Freq1" <4>
METRIC_INSTANCE                        4  Class: 3, Recorder: "" <8589934592>, Scope: SYSTEM_TREE_NODE "tegra-ubuntu" <1>

Metric class of "PAPI_L1_DCM", "PAPI_L2_DCM", "PAPI_L2_DCH" is 0
MerticInstance of "CPU_Freq2" is 2 and "CPU_Freq1" is 4
-------------------------------------------------------------------------------------------------------------------------------
