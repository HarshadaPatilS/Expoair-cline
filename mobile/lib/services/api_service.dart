import 'package:dio/dio.dart';
import 'package:flutter/material.dart';

// Assuming you have a Config class with a const BASE_URL variable in       
lib/config.dart
import 'config.dart';

class ApiService {
  static final _instance = ApiService._internal();

  // Private constructor to prevent instantiation from outside
  ApiService._internal();

  // Static method to get the singleton instance
  static ApiService get instance => _instance;

  final Dio dio = Dio();

  Future<Map> getAqi(double lat, double lon, String deviceId) async {
    try {
      Response response = await dio.get(
        Uri.parse('$BASE_URL/aqi'),
        queryParameters: {
          'lat': lat,
          'lon': lon,
          'deviceId': deviceId,
        },
      );
      return response.data;
    } catch (e) {
      if (e is DioException) {
        print('Error fetching AQI data: ${e.message}');
      }
      return {};
    }
  }

  Future<Map> getDose(String userId, double lat, double lon, String
activity, int durationMinutes) async {
    try {
      Response response = await dio.get(
        Uri.parse('$BASE_URL/dose'),
        queryParameters: {
          'userId': userId,
          'lat': lat,
          'lon': lon,
          'activity': activity,
          'durationMinutes': durationMinutes,
        },
      );
      return response.data;
    } catch (e) {
      if (e is DioException) {
        print('Error fetching dose data: ${e.message}');
      }
      return {};
    }
  }

  Future<List> getForecast(double lat, double lon) async {
(
        Uri.parse('$BASE_URL/forecast'),
        queryParameters: {
          'lat': lat,
          'lon': lon,
        },
      );
      return response.data;
    } catch (e) {
      if (e is DioException) {
        print('Error fetching
forecast data: ${e.message}');
      }
      return [];
    }
  }
}