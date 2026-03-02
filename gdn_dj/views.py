# gdn_dj/gdn_dj/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# 导航栏数据接口（前端调用这个接口就能拿到数据）
@csrf_exempt  # 调试阶段关闭CSRF校验，避免前端请求报错
def get_nav_items(request):
    # 把你前端的navItems转换成Python字典格式（直接复制用）
    nav_items = [
        {
            "name": "综合态势",
            "name": "综合态势",
            "cards": [
                {
                    "title": "游客态势",
                    "title": "游客态势",
                    "position": "left",
                    "barChart": {
                        "labels": ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"],
                    "barChart": {
                        "labels": ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"],
                        "datasets": [{
                            "label": "月度访问量",
                            "data": [1300, 1850, 1350, 1900, 2400, 2100, 3100, 3600, 2900, 1800, 1600, 950],
                            "data": [1300, 1850, 1350, 1900, 2400, 2100, 3100, 3600, 2900, 1800, 1600, 950],
                            "borderColor": "#4fc3f7",
                            "backgroundColor": "rgba(79, 195, 247, 0.6)",
                            "borderWidth": 1,
                            "borderRadius": 4,
                            "borderSkipped": False
                            "backgroundColor": "rgba(79, 195, 247, 0.6)",
                            "borderWidth": 1,
                            "borderRadius": 4,
                            "borderSkipped": False
                        }]
                    }
                },
                {
                    "title": "园区概览",
                    "position": "right",
                    "content": "入驻企业：128家\n就业人数：8,500人\n年产值：15.6亿\n绿化覆盖率：42%"
                    "position": "right",
                    "content": "入驻企业：128家\n就业人数：8,500人\n年产值：15.6亿\n绿化覆盖率：42%"
                },
                {
                    "title": "交通态势",
                    "position": "left",
                    "lineChart": {
                        "labels": ["早高峰", "平峰期", "晚高峰", "夜间"],
                    "title": "交通态势",
                    "position": "left",
                    "lineChart": {
                        "labels": ["早高峰", "平峰期", "晚高峰", "夜间"],
                        "datasets": [{
                            "label": "平均车速(km/h)",
                            "data": [35, 45, 30, 55],
                            "borderColor": "#4caf50",
                            "backgroundColor": "rgba(76, 175, 80, 0.2)",
                            "label": "平均车速(km/h)",
                            "data": [35, 45, 30, 55],
                            "borderColor": "#4caf50",
                            "backgroundColor": "rgba(76, 175, 80, 0.2)",
                            "tension": 0.3,
                            "fill": True
                        }]
                    }
                },
                {
                    "title": "园区活动",
                    "title": "园区活动",
                    "position": "right",
                    "activities": [
                        {"title": "月度安全会议", "time": "今天 14:00", "status": "待开始", "location": "会议室A", "type": "meeting"},
                        {"title": "设备例行维护", "time": "明天 09:00", "status": "待开始", "location": "B区机房", "type": "maintenance"},
                        {"title": "园区安全巡检", "time": "02-29 10:30", "status": "进行中", "location": "全园区", "type": "inspection"},
                        {"title": "新员工培训", "time": "03-01 15:00", "status": "待开始", "location": "培训中心", "type": "training"},
                        {"title": "消防设施检查", "time": "03-02 11:00", "status": "待开始", "location": "各楼层", "type": "inspection"}
                    ]
                    "activities": [
                        {"title": "月度安全会议", "time": "今天 14:00", "status": "待开始", "location": "会议室A", "type": "meeting"},
                        {"title": "设备例行维护", "time": "明天 09:00", "status": "待开始", "location": "B区机房", "type": "maintenance"},
                        {"title": "园区安全巡检", "time": "02-29 10:30", "status": "进行中", "location": "全园区", "type": "inspection"},
                        {"title": "新员工培训", "time": "03-01 15:00", "status": "待开始", "location": "培训中心", "type": "training"},
                        {"title": "消防设施检查", "time": "03-02 11:00", "status": "待开始", "location": "各楼层", "type": "inspection"}
                    ]
                }
            ]
        },
        {
            "name": "园测数据",
            "name": "园测数据",
            "cards": [
                {
                    "title": "风控要素",
                    "title": "风控要素",
                    "position": "left",
                    "progressBar": [
                        {"label": "安全风险评估", "value": 78},
                        {"label": "威胁检测准备", "value": 92},
                        {"label": "应急响应速度", "value": 85},
                        {"label": "系统防护强度", "value": 88},
                        {"label": "合规性检查", "value": 95}
                    ]
                    "progressBar": [
                        {"label": "安全风险评估", "value": 78},
                        {"label": "威胁检测准备", "value": 92},
                        {"label": "应急响应速度", "value": 85},
                        {"label": "系统防护强度", "value": 88},
                        {"label": "合规性检查", "value": 95}
                    ]
                },
                {
                    "title": "环境监测数据",
                    "title": "环境监测数据",
                    "position": "left",
                    "environmentData": [
                        {"name": "空气质量指数", "value": 45, "level": "优", "unit": "AQI"},
                        {"name": "PM2.5浓度", "value": 25, "level": "良", "unit": "μg/m³"},
                        {"name": "噪声水平", "value": 55, "level": "良", "unit": "dB"},
                        {"name": "温湿度", "value": "26℃/65%", "level": "舒适", "unit": ""},
                        {"name": "光照强度", "value": 850, "level": "充足", "unit": "lux"}
                    ]
                },
                {
                    "title": "传感器状态",
                    "position": "right",
                    "listData": [
                        {"deviceId": "SN-001", "location": "园区东门", "status": "正常", "time": "15:30:22"},
                        {"deviceId": "SN-002", "location": "主楼大厅", "status": "预警", "time": "15:28:15"},
                        {"deviceId": "SN-003", "location": "停车场A区", "status": "正常", "time": "15:25:40"},
                        {"deviceId": "SN-004", "location": "园区西门", "status": "故障", "time": "15:22:18"},
                        {"deviceId": "SN-005", "location": "绿化带区域", "status": "正常", "time": "15:20:33"},
                        {"deviceId": "SN-006", "location": "餐厅门口", "status": "正常", "time": "15:18:45"}
                    ]
                },
                    "environmentData": [
                        {"name": "空气质量指数", "value": 45, "level": "优", "unit": "AQI"},
                        {"name": "PM2.5浓度", "value": 25, "level": "良", "unit": "μg/m³"},
                        {"name": "噪声水平", "value": 55, "level": "良", "unit": "dB"},
                        {"name": "温湿度", "value": "26℃/65%", "level": "舒适", "unit": ""},
                        {"name": "光照强度", "value": 850, "level": "充足", "unit": "lux"}
                    ]
                },
                {
                    "title": "传感器状态",
                    "position": "right",
                    "listData": [
                        {"deviceId": "SN-001", "location": "园区东门", "status": "正常", "time": "15:30:22"},
                        {"deviceId": "SN-002", "location": "主楼大厅", "status": "预警", "time": "15:28:15"},
                        {"deviceId": "SN-003", "location": "停车场A区", "status": "正常", "time": "15:25:40"},
                        {"deviceId": "SN-004", "location": "园区西门", "status": "故障", "time": "15:22:18"},
                        {"deviceId": "SN-005", "location": "绿化带区域", "status": "正常", "time": "15:20:33"},
                        {"deviceId": "SN-006", "location": "餐厅门口", "status": "正常", "time": "15:18:45"}
                    ]
                },
                {
                    "title": "雨水监测",
                    "title": "雨水监测",
                    "position": "right",
                    "barChart": {
                        "labels": ["02-24", "02-25", "02-26", "02-27", "02-28", "02-29", "03-01"],
                    "barChart": {
                        "labels": ["02-24", "02-25", "02-26", "02-27", "02-28", "02-29", "03-01"],
                        "datasets": [{
                            "label": "降雨量(mm)",
                            "data": [0, 0, 3, 18, 0, 0, 0],
                            "backgroundColor": [
                                "rgba(33, 150, 243, 0.3)",
                                "rgba(33, 150, 243, 0.3)",
                                "rgba(33, 150, 243, 0.66)",
                                "rgba(33, 150, 243, 0.9)",
                                "rgba(33, 150, 243, 0.3)",
                                "rgba(33, 150, 243, 0.3)",
                                "rgba(33, 150, 243, 0.3)"
                            ],
                            "borderColor": "#2196f3",
                            "borderWidth": 1,
                            "borderRadius": 6,
                            "borderSkipped": False,
                            "hoverBackgroundColor": "rgba(33, 150, 243, 0.9)",
                            "hoverBorderColor": "#ffffff",
                            "hoverBorderWidth": 2
                        }]
                    }
                            "label": "降雨量(mm)",
                            "data": [0, 0, 3, 18, 0, 0, 0],
                            "backgroundColor": [
                                "rgba(33, 150, 243, 0.3)",
                                "rgba(33, 150, 243, 0.3)",
                                "rgba(33, 150, 243, 0.66)",
                                "rgba(33, 150, 243, 0.9)",
                                "rgba(33, 150, 243, 0.3)",
                                "rgba(33, 150, 243, 0.3)",
                                "rgba(33, 150, 243, 0.3)"
                            ],
                            "borderColor": "#2196f3",
                            "borderWidth": 1,
                            "borderRadius": 6,
                            "borderSkipped": False,
                            "hoverBackgroundColor": "rgba(33, 150, 243, 0.9)",
                            "hoverBorderColor": "#ffffff",
                            "hoverBorderWidth": 2
                        }]
                    }
                }
            ]
        },
        {
            "name": "安防监控",
            "name": "安防监控",
            "cards": [
                {
                    "title": "监控画面",
                    "position": "right",
                    "gridData": [
                        {"id": "CAM-001", "location": "东门入口", "status": "在线", "time": "15:30"},
                        {"id": "CAM-002", "location": "西门出口", "status": "在线", "time": "15:30"},
                        {"id": "CAM-003", "location": "北区停车场", "status": "离线", "time": "02-27 15:25"},
                        {"id": "CAM-004", "location": "南区花园", "status": "在线", "time": "15:30"},
                        {"id": "CAM-005", "location": "中央大厅", "status": "维护中", "time": "N/A"},
                        {"id": "CAM-006", "location": "办公区走廊", "status": "在线", "time": "15:30"},
                        {"id": "CAM-007", "location": "餐厅区域", "status": "在线", "time": "15:30"},
                        {"id": "CAM-008", "location": "健身房入口", "status": "在线", "time": "15:30"}
                    ]
                    "title": "监控画面",
                    "position": "right",
                    "gridData": [
                        {"id": "CAM-001", "location": "东门入口", "status": "在线", "time": "15:30"},
                        {"id": "CAM-002", "location": "西门出口", "status": "在线", "time": "15:30"},
                        {"id": "CAM-003", "location": "北区停车场", "status": "离线", "time": "02-27 15:25"},
                        {"id": "CAM-004", "location": "南区花园", "status": "在线", "time": "15:30"},
                        {"id": "CAM-005", "location": "中央大厅", "status": "维护中", "time": "N/A"},
                        {"id": "CAM-006", "location": "办公区走廊", "status": "在线", "time": "15:30"},
                        {"id": "CAM-007", "location": "餐厅区域", "status": "在线", "time": "15:30"},
                        {"id": "CAM-008", "location": "健身房入口", "status": "在线", "time": "15:30"}
                    ]
                },
                {
                    "title": "入侵检测统计",
                    "title": "入侵检测统计",
                    "position": "left",
                    "intrusionData": [
                        {"type": "人员入侵", "count": 12, "trend": "上升", "level": "warning"},
                        {"type": "车辆闯入", "count": 3, "trend": "稳定", "level": "normal"},
                        {"type": "周界突破", "count": 1, "trend": "下降", "level": "critical"},
                        {"type": "异常行为", "count": 8, "trend": "上升", "level": "warning"},
                        {"type": "非法停留", "count": 5, "trend": "稳定", "level": "normal"}
                    ]
                },
                {
                    "title": "园区监控",
                    "position": "left",
                    "listData": [
                        {"deviceId": "CAM-001", "location": "东门入口", "status": "在线", "time": "03-01 15:30"},
                        {"deviceId": "CAM-002", "location": "西门出口", "status": "在线", "time": "03-01 15:30"},
                        {"deviceId": "CAM-003", "location": "北区停车场", "status": "离线", "time": "02-27 15:25"},
                        {"deviceId": "CAM-004", "location": "南区花园", "status": "在线", "time": "03-01 15:30"},
                        {"deviceId": "CAM-005", "location": "中央大厅", "status": "维护中", "time": "N/A"},
                        {"deviceId": "CAM-007", "location": "餐厅区域", "status": "在线", "time": "03-01 15:30"},
                        {"deviceId": "CAM-008", "location": "健身房入口", "status": "在线", "time": "03-01 15:30"}
                    ]
                    "intrusionData": [
                        {"type": "人员入侵", "count": 12, "trend": "上升", "level": "warning"},
                        {"type": "车辆闯入", "count": 3, "trend": "稳定", "level": "normal"},
                        {"type": "周界突破", "count": 1, "trend": "下降", "level": "critical"},
                        {"type": "异常行为", "count": 8, "trend": "上升", "level": "warning"},
                        {"type": "非法停留", "count": 5, "trend": "稳定", "level": "normal"}
                    ]
                },
                {
                    "title": "园区监控",
                    "position": "left",
                    "listData": [
                        {"deviceId": "CAM-001", "location": "东门入口", "status": "在线", "time": "03-01 15:30"},
                        {"deviceId": "CAM-002", "location": "西门出口", "status": "在线", "time": "03-01 15:30"},
                        {"deviceId": "CAM-003", "location": "北区停车场", "status": "离线", "time": "02-27 15:25"},
                        {"deviceId": "CAM-004", "location": "南区花园", "status": "在线", "time": "03-01 15:30"},
                        {"deviceId": "CAM-005", "location": "中央大厅", "status": "维护中", "time": "N/A"},
                        {"deviceId": "CAM-007", "location": "餐厅区域", "status": "在线", "time": "03-01 15:30"},
                        {"deviceId": "CAM-008", "location": "健身房入口", "status": "在线", "time": "03-01 15:30"}
                    ]
                }
            ]
        },
        {
            "name": "能源管理",
            "name": "能源管理",
            "cards": [
                {
                    "title": "能耗分析",
                    "title": "能耗分析",
                    "position": "left",
                    "gaugeChart": {
                        "minValue": 0,
                        "maxValue": 100,
                        "currentValue": 68.5,
                        "unit": "%"
                    }
                    "gaugeChart": {
                        "minValue": 0,
                        "maxValue": 100,
                        "currentValue": 68.5,
                        "unit": "%"
                    }
                },
                {
                    "title": "电力负荷",
                    "title": "电力负荷",
                    "position": "right",
                    "lineChart": {
                        "labels": ["峰时", "平时", "谷时"],
                    "lineChart": {
                        "labels": ["峰时", "平时", "谷时"],
                        "datasets": [{
                            "label": "用电负荷(kW)",
                            "data": [850, 620, 380],
                            "borderColor": "#ff9800",
                            "backgroundColor": "rgba(255, 152, 0, 0.2)",
                            "label": "用电负荷(kW)",
                            "data": [850, 620, 380],
                            "borderColor": "#ff9800",
                            "backgroundColor": "rgba(255, 152, 0, 0.2)",
                            "tension": 0.3,
                            "fill": True
                        }]
                    }
                }
            ]
        }
    ]
    
    # 返回JSON数据，支持中文，兼容列表格式
    return JsonResponse(nav_items, json_dumps_params={'ensure_ascii': False}, safe=False)