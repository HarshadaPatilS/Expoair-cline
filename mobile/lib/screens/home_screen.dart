import 'package:provider/provider.dart';

class HealthScore {
  String name;
  int score;

  HealthScore({required this.name, required this.score});
}

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState()
=> _HomeScreenState();
}

class _HomeScreenState extends
State<HomeScreen> {
  final double aqiValue = 120; //
Dummy AQI value
  final int pm25Value = 40;   //
Dummy PM2.5 value
  HealthScore healthScore = HealthScore(name: 'John Doe', score: 70);       
// Dummy HealthScore

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Home Screen'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            AnimatedContainer(
              duration: Duration(milliseconds: 300),
              width: 150.0,
              height: 150.0,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: _getAQIColor(aqiValue),
              ),
              child: Center(
                child: Text(
                  'AQI $aqiValue',
                  style: TextStyle(fontSize: 24.0, fontWeight:
FontWeight.bold),
                ),
              ),
            ),
            SizedBox(height: 16.0),
            Row(
              children: [
                Icon(Icons.air_pollution),
                Padding(
                  padding: const EdgeInsets.only(left: 8.0),
                  child: Text('PM2.5 $pm25Value'),
                ),
              ],
            ),
            SizedBox(height: 16.0),
            Text(
              'Health Score: ${healthScore.score}',
              style: TextStyle(fontSize: 18.0, fontWeight: 
FontWeight.bold),
            ),
            SizedBox(height: 32.0),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                IconButton(
                  icon: Icon(Icons.map),
                  onPressed: () {
                    // Navigate to Map screen
                  },
                ),
                IconButton(
                  icon: Icon(Icons.history),
                  onPressed: () {
                    // Navigate to History screen
                  },
                ),
                IconButton(
                  icon: Icon(Icons.settings),
                  onPressed: () {
                    // Navigate to Settings screen
                  },
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Color _getAQIColor(double aqiValue) {
    if (aqiValue < 50) return Colors.green;
    else if (aqiValue < 100) return Colors.yellow;
    else if (aqiValue < 150) return Colors.orange;
    else return Colors.red;
  }
}