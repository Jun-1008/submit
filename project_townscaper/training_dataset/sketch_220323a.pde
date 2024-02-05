// --------------------------------------------------------------------
// Load a save file from Townscaper as a template, replace the voxel
// data, then save the file out with a timestamp.
// --------------------------------------------------------------------

import java.lang.Float;
import java.text.SimpleDateFormat;
import java.util.Date;

// Offsets in noise space for attributes.
final static float BUILDING_HEIGHT_NOISE_OFFSET = 0.0;
final static float BUILDING_COLOR_NOISE_OFFSET = 25.0;
final static float STRUT_HEIGHT_NOISE_OFFSET = 50.0;

// Noise distribution (larger values -> more variation).
 final static float BUILDING_HEIGHT_NOISE_RANGE = 200.0;
//final static float BUILDING_HEIGHT_NOISE_RANGE = 5.0;
// final static float BUILDING_COLOR_NOISE_RANGE = 1.0;
final static float BUILDING_COLOR_NOISE_RANGE = 5.0;
// final static float STRUT_HEIGHT_NOISE_RANGE = 20.0;
final static float STRUT_HEIGHT_NOISE_RANGE = 200.0;

// Value ranges.
final static float MAX_BUILDING_HEIGHT = 14.0;
//final static float MAX_BUILDING_HEIGHT = 3.0;
final static float MAX_BUILDING_COLOR = 15;
final static float MAX_STRUT_HEIGHT = 0.0;


XML xml;
XML[] corners;
XML voxelHolder;
// float minX, maxX, minY, maxY;
float minX, maxX, minY, maxY, buildingHeight;
float xRange, yRange;

void loadTownFile() {
  for (int j=0; j<1000; j++) {
    // The code expects a file called "Town0.scape" to be located in the project's "data" folder.このコードでは、プロジェクトの "data "フォルダに "Town0.scape "というファイルが存在することを想定しています。
    xml = loadXML("25x25.scape");

    // Load the corner array.
    XML cornerHolder = xml.getChild("corners");
    corners = cornerHolder.getChildren("C");

    // Traverse the corner array to find the range for X and Y coordinates.
    minX = minY = Float.MAX_VALUE;
    maxX = maxY = Float.MIN_VALUE;

    for (int i=0; i<corners.length; i++) {
      float x = corners[i].getChild("x").getFloatContent();
      float y = corners[i].getChild("y").getFloatContent();

      minX = min(minX, x);
      maxX = max(maxX, x);

      minY = min(minY, y);
      maxY = max(maxY, y);
    }

    println("X Range: " + minX + " - " + maxX);
    println("Y Range: " + minY + " - " + maxY);

    xRange = (maxX - minX);
    yRange = (maxY - minY);

    // Load the voxel array.
    voxelHolder = xml.getChild("voxels");
    XML[] voxels = voxelHolder.getChildren("V");

    // Remove all existing voxels.
    for (int i=0; i<voxels.length; i++) {
      voxelHolder.removeChild(voxels[i]);
    }



    // void generateTownMap() {

    for (int c=0; c<corners.length; c++) {
      // Get the X and Y of the corner, normalized so 0 is the minimum.
      float normalizedX = minX + corners[c].getChild("x").getFloatContent();
      float normalizedY = minY + corners[c].getChild("y").getFloatContent();

      // Calculate the building height.
      int buildingHeight = 1 + (int)(noise(BUILDING_HEIGHT_NOISE_OFFSET + (normalizedX+j) / (xRange+j) * BUILDING_HEIGHT_NOISE_RANGE, BUILDING_HEIGHT_NOISE_OFFSET + (normalizedY+j) / (yRange+j) * BUILDING_HEIGHT_NOISE_RANGE) * MAX_BUILDING_HEIGHT);
      // println(buildingHeight);
      corners[c].getChild("count").setContent(str(buildingHeight));
      // println(buildingHeight);

      // Calculate strut height
      int strutHeight = (int)(noise(STRUT_HEIGHT_NOISE_OFFSET + (normalizedX+j) / (xRange+j) * STRUT_HEIGHT_NOISE_RANGE, STRUT_HEIGHT_NOISE_OFFSET + (normalizedY+j) / (yRange+j) * STRUT_HEIGHT_NOISE_RANGE) * MAX_STRUT_HEIGHT);

      for (int v=0; v<buildingHeight; v++) {
        // Calculate color
        int voxColor = (int)(noise(BUILDING_COLOR_NOISE_OFFSET + normalizedX / xRange * BUILDING_COLOR_NOISE_RANGE, BUILDING_COLOR_NOISE_OFFSET + normalizedY / yRange * BUILDING_COLOR_NOISE_RANGE) * MAX_BUILDING_COLOR);

        // Add the voxel to the array and set the color and height attributes.
        XML genVoxel = voxelHolder.addChild("V");
        XML colorEl = genVoxel.addChild("t");
        colorEl.setContent(str(voxColor));
        XML heightEl = genVoxel.addChild("h");
        heightEl.setContent(str(strutHeight + v));
      }
    }



    // void saveTownFile() {
    // Build a timestamped filename.
    final SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd_HH-mm-ss");
    final String timeStamp = format.format(new Date());
    //final String generatedXmlFileName = "Town" + timeStamp + ".scape";
    final String generatedXmlFileName = int(j) + ".scape";
    println(int(j));

    // Save the XML out.
    saveXML(xml, generatedXmlFileName);
  }
}

void setup() {
  loadTownFile();
  //generateTownMap();
  // saveTownFile();
}
