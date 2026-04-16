import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:geolocator/geolocator.dart';
import 
'package:flutter_map_marker_cluster/flutter_map_marker_cluster.dart';
import 'package:provider/provider.dart';

class MapScreen extends StatefulWidget {
  final double aqiValue;

  const MapScreen({Key? key, required this.aqiValue}) : super(key: 
key);

  @override
  _MapScreenState createState() => _MapScreenState();
}

class _MapScreenState extends State<MapScreen> {
  late Position currentLocation;
  late LatLng currentPosition;
  late Widget circleLayer;

  @override
  void initState() {
    super.initState();
    getLocation();
  }

  Future<void> getLocation() async {
    LocationPermission permission = await 
Geolocator.checkPermission();
    if (permission == 
LocationPermission.deniedForever) {
      return Future.error('Location permission denied forever');
    } else if (permission == LocationPermission.denied) {
      await Geolocator.requestPermission();
      if (await Geolocator.checkPermission() != 
LocationPermission.always) {
        return;
      }
    }

    Position position = await 
Geolocator.getCurrentPosition(desiredAccuracy: LocationAccuracy.best);
    setState(() {
      currentLocation = position;
      currentPosition = LatLng(position.latitude, position.longitude);
    });

    circleLayer = CircleLayer(
      options: CircleLayerOptions(
        circles: [
          CircleMarker(
            width: 20,
            height: 20,
            point: currentPosition,
            color: _getAQIColor(widget.aqiValue),
          ),
        ],
      ),
    );
  }

  Color _getAQIColor(double aqiValue) {
    if (aqiValue < 50) return Colors.green;
    else if (aqiValue < 100) return Colors.yellow;
    else if (aqiValue < 150) return Colors.orange;
    else return Colors.red;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Map Screen'),
      ),
      body: FlutterMap(
        mapController: MapController(),
        options: MapOptions(
          center: currentPosition,
          zoom: 15.0,
        ),
        layers: [
          TileLayer(
            urlTemplate: 
'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            subdomains: ['a', 'b', 'c'],
          ),
          circleLayer,
        ],
      ),
      floatingActionButtonLocation: 
FloatingActionButtonLocation.centerBottom,
      floatingActionButton: ElevatedButton(
        onPressed: () {
          showSheet(context);
        },
        child: Text('Route Optimizer'),
      ),
    );
  }

  void showSheet(BuildContext context) {
    showModalBottomSheet(
      context: context,
      builder: (context) {
        return Container(
          height: 200.0,
          padding: const EdgeInsets.all(16.0),
          child: Column(
            children: [
              Text('Current AQI: ${widget.aqiValue}'),
              SizedBox(height: 8.0),
              Text('PM2.5: 40'), // Dummy PM2.5 value
              SizedBox(height: 16.0),
              ElevatedButton(
                onPressed: () {
                  Navigator.push(context, MaterialPageRoute(builder:        
(context) => RouteOptimizerScreen()));
                },
                child: Text('Route Optimizer'),
              ),
            ],
          ),
        );
      },
    );
  }
}

class RouteOptimizerScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Route Optimizer Screen'),
      ),
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            Navigator.pop(context);
          },
          child: Text('Back to Map'),
        ),
      ),
    );
  }
}