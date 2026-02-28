# gdn_dj/gdn_dj/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# 导航栏数据接口（前端调用这个接口就能拿到数据）
@csrf_exempt  # 调试阶段关闭CSRF校验，避免前端请求报错
def get_nav_items(request):
    # 把你前端的navItems转换成Python字典格式（直接复制用）
    nav_items = [
        {
            "name": "首页",
            "cards": [
                {
                    "title": "数据趋势图表",
                    "position": "left",
                    "chartData": {
                        "labels": ["1月", "2月", "3月", "4月", "5月", "6月"],
                        "datasets": [{
                            "label": "月度访问量",
                            "data": [1200, 1900, 1500, 2500, 2200, 3000],
                            "borderColor": "#4fc3f7",
                            "backgroundColor": "rgba(79, 195, 247, 0.2)",
                            "tension": 0.3,
                            "fill": True
                        }]
                    }
                },
                {
                    "title": "园区概览",
                    "position": "left",
                    "content": "设备在线率：98%\n环境温度：25℃\n湿度：60%\n风速：2m/s"
                },
                {
                    "title": "设备状态",
                    "position": "right",
                    "chartData": {
                        "labels": ["照明", "监控", "传感器", "其他"],
                        "datasets": [{
                            "label": "设备数量",
                            "data": [56, 32, 18, 10],
                            "borderColor": "#9ccc65",
                            "backgroundColor": "rgba(156, 204, 101, 0.2)",
                            "tension": 0.3,
                            "fill": True
                        }]
                    }
                },
                {
                    "title": "环境监测",
                    "position": "right",
                    "content": "温度：25℃\n湿度：60%\n风速：2m/s\n气压：1013hPa"
                }
            ]
        },
        {
            "name": "数据监控",
            "cards": [
                {
                    "title": "能耗分析",
                    "position": "left",
                    "chartData": {
                        "labels": ["周一", "周二", "周三", "周四", "周五", "周六"],
                        "datasets": [{
                            "label": "日能耗(kWh)",
                            "data": [200, 250, 300, 280, 320, 260],
                            "borderColor": "#ff9800",
                            "backgroundColor": "rgba(255, 152, 0, 0.2)",
                            "tension": 0.3,
                            "fill": True
                        }]
                    }
                },
                {
                    "title": "运行时长统计",
                    "position": "left",
                    "content": "总运行时长：1200小时\n平均时长：12小时\n最长：照明系统"
                },
                {
                    "title": "报警记录",
                    "position": "right",
                    "chartData": {
                        "labels": ["紧急", "重要", "一般", "提示"],
                        "datasets": [{
                            "label": "报警次数",
                            "data": [0, 1, 5, 6],
                            "borderColor": "#f44336",
                            "backgroundColor": "rgba(244, 67, 54, 0.2)",
                            "tension": 0.3,
                            "fill": True
                        }]
                    }
                },
                {
                    "title": "历史数据",
                    "position": "right",
                    "content": "昨日能耗：1180kWh\n上周同期：1250kWh\n上月同期：32000kWh"
                }
            ]
        },
        {
            "name": "设备管理",
            "cards": [
                {
                    "title": "设备分布",
                    "position": "left",
                    "chartData": {
                        "labels": ["A区", "B区", "C区", "D区"],
                        "datasets": [{
                            "label": "设备密度",
                            "data": [28, 35, 22, 21],
                            "borderColor": "#9c27b0",
                            "backgroundColor": "rgba(156, 39, 176, 0.2)",
                            "tension": 0.3,
                            "fill": True
                        }]
                    }
                },
                {
                    "title": "设备清单",
                    "position": "left",
                    "content": "1. 照明设备（56台）\n2. 监控设备（32台）\n3. 环境传感器（18台）\n4. 其他设备（10台）",
                },
                {
                    "title": "维护计划",
                    "position": "right",
                    "chartData": {
                        "labels": ["待处理", "处理中", "已完成"],
                        "datasets": [{
                            "label": "维护任务",
                            "data": [3, 8, 15],
                            "borderColor": "#00bcd4",
                            "backgroundColor": "rgba(0, 188, 212, 0.2)",
                            "tension": 0.3,
                            "fill": True
                        }]
                    }
                },
                {
                    "title": "设备详情",
                    "position": "right",
                    "content": "最新上线：摄像头007\n最近离线：传感器012\n故障修复：照明023"
                }
            ]
        },
        {
            "name": "系统设置",
            "cards": [
                {
                    "title": "性能监控",
                    "position": "left",
                    "chartData": {
                        "labels": ["CPU", "内存", "磁盘", "网络"],
                        "datasets": [{
                            "label": "使用率(%)",
                            "data": [45, 65, 30, 75],
                            "borderColor": "#e91e63",
                            "backgroundColor": "rgba(233, 30, 99, 0.2)",
                            "tension": 0.3,
                            "fill": True
                        }]
                    }
                },
                {
                    "title": "用户管理",
                    "position": "left",
                    "content": "在线用户：3人\n总用户数：12人\n活跃用户：8人"
                },
                {
                    "title": "备份状态",
                    "position": "right",
                    "chartData": {
                        "labels": ["成功", "失败", "进行中"],
                        "datasets": [{
                            "label": "备份次数",
                            "data": [15, 2, 1],
                            "borderColor": "#8bc34a",
                            "backgroundColor": "rgba(139, 195, 74, 0.2)",
                            "tension": 0.3,
                            "fill": True
                        }]
                    }
                },
                {
                    "title": "系统信息",
                    "position": "right",
                    "content": "系统版本：v2.1.0\n运行时间：15天\n最后重启：2026-01-03"
                }
            ]
        }
    ]
    
    # 返回JSON数据，支持中文，兼容列表格式
    return JsonResponse(nav_items, json_dumps_params={'ensure_ascii': False}, safe=False)