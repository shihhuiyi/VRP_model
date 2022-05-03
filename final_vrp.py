# %%
import pandas as pd
import folium
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

taipei = [25.053629,121.5408] # 台北區平均座標，用來設定地圖原始位置
newtaipei = [25.030308482499997,121.474837065] # 新北區平均座標，用來設定地圖原始位置
city = "new_taipei" # 現在要跑的區域
num_vehicles = 3 # 車輛數，若設為1即為tsp

if city == "taipei":
    df = pd.read_csv("taipei_distance.csv",index_col=0)
    local = taipei
else:
    df = pd.read_csv("newtaipei_distance_1.csv",index_col=0)
    local = newtaipei
df1 = pd.read_csv("分行特性表1.csv")


def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = df.values # 區域距離矩陣
    data['num_vehicles'] = num_vehicles # 車輛數
    if city == "taipei": # 設定區域中心位置
        data['depot'] = list(df.columns).index("121")
    else:
        data['depot'] = list(df.columns).index("117")
    return data


def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    print(f'Objective: {solution.ObjectiveValue()}')
    max_route_distance = 0
    plan = {}
    # 求每個車輛的最佳路徑
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_distance = 0
        node = []
        while not routing.IsEnd(index):
            #plan_output += ' {} -> '.format(manager.IndexToNode(index))
            plan_output += " bank {} ->".format(df.index[manager.IndexToNode(index)])
            node.append(df.index[manager.IndexToNode(index)])
            #print(df.index[manager.IndexToNode(index)])
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)
        #plan_output += '{}\n'.format(manager.IndexToNode(index))
        plan_output += " bank {} \n->".format(df.index[manager.IndexToNode(index)])
        plan_output += 'Distance of the route: {}km\n'.format(route_distance)
        print(plan_output)
        max_route_distance = max(route_distance, max_route_distance)
        plan[vehicle_id] = node
    print('Maximum of the route distances: {}km'.format(max_route_distance))
    print_map(plan)

def print_map(plan):
    # 將最佳路徑於地圖上呈現
    m =folium.Map(
        location=local, # 地圖起始位置
        titles= city, # 區域
        zoom_start= 12.5,  #地圖起始縮放比例
    )
    # 把每個車輛路徑畫在地圖上
    for _, vehicle in plan.items():
        t=0
        # color_list = ["blue","purple","darkgreen"]
        # 不同車輛路徑用不同顏色區隔
        color_list =  ['blue', 'purple', 'darkgreen', 'darkred', 'lightred', 'beige', 'darkblue', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']
        for node in vehicle:
            # 地圖上標記分行位置
            location=[df1[df1["分行代碼"]==node]["lat"].values[0], df1[df1["分行代碼"]==node]["lon"].values[0]]
            if t == 0:
                # 調度中心用紅色點標記
                folium.Marker(
                    location,
                    popup= "bank {}".format(node),
                    icon=folium.Icon(color="red",icon='fa-truck', prefix='fa')
                ).add_to(m)
                _location = location

            else:
                # 標記其餘的分行
                folium.Marker(
                    location,
                    popup= "bank {}".format(node),
                    icon=folium.Icon(color=color_list[_],icon='fa-truck', prefix='fa')
                ).add_to(m)
                # 依照運補順序將分行連線，線的顏色與分行點顏色相同
                folium.PolyLine(
                    [_location,location],
                    color=color_list[_],
                    weight=4,
                    opacity=0.5
                ).add_to(m)
                _location = location
            t+=1
    # 用html儲存地圖
    m.save("map.html")


def main():
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint.
    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        3000,  # 每個路徑的距離上線，目前設置3000km=沒有上限
        True,  # start cumul to zero
        dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100) # 為距離轉換為成本的係數

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC) # 使用最小成本，即最短路徑

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(data, manager, routing, solution)
    else:
        print('No solution found !')


if __name__ == '__main__':
    main()
# %%
