import SegmentStatistics
import slicer

# Get your nodes (use exact names from your scene)
segmentationNode = slicer.util.getNode('Segmentation')  # Your segmentation
volumeNode = slicer.util.getNode('CTChest')  # Your volume

# Setup statistics logic
segStatLogic = SegmentStatistics.SegmentStatisticsLogic()
paramNode = segStatLogic.getParameterNode()

# Set parameters - THIS IS THE CORRECT METHOD [citation:1]
paramNode.SetParameter("Segmentation", segmentationNode.GetID())
paramNode.SetParameter("ScalarVolume", volumeNode.GetID())

# Compute statistics
segStatLogic.computeStatistics()

# Get the statistics as a dictionary
statistics = segStatLogic.getStatistics()

# Print results to console
print("\n" + "="*50)
print("VOLUME CALCULATION RESULTS")
print("="*50)

for segmentId in statistics["SegmentIDs"]:
    # Get volume in mm3
    volume_mm3 = statistics[segmentId, "LabelmapSegmentStatisticsPlugin.volume_mm3"]
    volume_cm3 = volume_mm3 / 1000
    
    # Get segment name
    segment = segmentationNode.GetSegmentation().GetSegment(segmentId)
    segmentName = segment.GetName()
    
    print(f"{segmentName}: {volume_mm3:.2f} mm³ ({volume_cm3:.2f} cm³)")

print("="*50)