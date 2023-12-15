def sort_mahjong_tiles(hand_tiles):
    # 定义花色的优先级
    suit_order = {'bamboo': 1, 'char': 2, 'dot': 3}

    # 定义点数的优先级
    rank_order = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    # 根据花色和点数的优先级进行排序
    sorted_tiles = sorted(hand_tiles, key=lambda x: (suit_order[x.split('_')[0]], rank_order[x.split('_')[1]]))

    return sorted_tiles

# 将花色拆分出来，用数值表示点数
def split_suit_and_convert_to_numeric(sorted_hand):
    bamboo = []
    char = []
    dot = []

    for tile in sorted_hand:
        suit, rank = tile.split('_')
        rank_numeric = int(rank)
            
        if suit == 'bamboo':
            bamboo.append(rank_numeric)
        elif suit == 'char':
            char.append(rank_numeric)
        elif suit == 'dot':
            dot.append(rank_numeric)

    return bamboo, char, dot

def extract_all_triplet_combinations(suit_tiles):
    all_combinations = []
    triplets = [(i, i+1, i+2) for i in range(1, 8)]  # 生成所有可能的搭子
    triplets.extend([(i, i, i) for i in range(1, 10)])  # 三张一样数字的搭子
    max_triplet_count = 0  # Track the maximum triplet count

    def find_triplets_recursive(current_sets, current_remaining_tiles):
        nonlocal all_combinations, max_triplet_count

        # If current_sets is not empty, add the combination to the list
        if current_sets:
            triplet_count = len(current_sets)
            if triplet_count > max_triplet_count:
                all_combinations.clear()  # Remove previous combinations with fewer triplets
                all_combinations.append((current_sets, current_remaining_tiles))
                max_triplet_count = triplet_count
            elif triplet_count == max_triplet_count:
                all_combinations.append((current_sets, current_remaining_tiles))

        for i, triplet in enumerate(triplets):
            # Create a copy of current sets and remaining tiles
            sets_copy = current_sets.copy()
            remaining_tiles_copy = current_remaining_tiles.copy()

            # Check if the triplet is a valid match
            if all(triplet.count(tile) <= remaining_tiles_copy.count(tile) for tile in triplet) and all(
                    remaining_tiles_copy.count(tile) < 4 for tile in triplet):
                # Append the current triplet to the sets copy
                sets_copy.append(list(triplet))

                # Remove tiles of the triplet from remaining tiles copy
                for tile in triplet:
                    remaining_tiles_copy.remove(tile)

                # Recursively find triplets in the updated state
                find_triplets_recursive(sets_copy, remaining_tiles_copy)

    # Start the recursive process
    find_triplets_recursive([], suit_tiles)
    
    return all_combinations

def extract_all_pair_combinations(triplet_combinations):
    sets, remaining_tiles = triplet_combinations
    all_pair_combinations = []

    pairs = [(i, i) for i in range(1, 10)]  # 生成所有可能的对子

    found_pairs = False

    for pair in pairs:
        pair_sets = []
        # 确保对子的牌数量满足条件
        if all(pair.count(tile) <= remaining_tiles.count(tile) for tile in pair):
            pair_sets.append(list(pair))  # 提取对子
            found_pairs = True
            # 逐个减去每个组合中出现的数字
            for tile in pair:
                remaining_tiles.remove(tile)
            all_pair_combinations.append((sets.copy(), pair_sets, remaining_tiles.copy()))

    if not found_pairs:
        # 没有找到对子，返回一个空白的对子组合列表
        all_pair_combinations.append((sets.copy(), [], remaining_tiles.copy()))

    return all_pair_combinations

def extract_all_kao_combinations(pair_combinations):
    sets, pairs, remaining_tiles = pair_combinations
    all_kao_combinations = []

    kaos = [(i, i+1) for i in range(1, 9)]  # 生成所有可能的靠张

    found_kaos = False

    for kao in kaos:
        kao_sets = []
        # 确保靠张的牌数量满足条件
        if all(kao.count(tile) <= remaining_tiles.count(tile) for tile in kao):
            kao_sets.append(list(kao))  # 提取靠张
            found_kaos = True
            # 逐个减去每个组合中出现的数字
            for tile in kao:
                remaining_tiles.remove(tile)
            all_kao_combinations.append((sets.copy(), pairs.copy(), kao_sets, remaining_tiles.copy()))

    if not found_kaos:
        # 没有找到靠张，返回一个空白的靠张组合列表
        all_kao_combinations.append((sets.copy(), pairs.copy(), [], remaining_tiles.copy()))

    return all_kao_combinations

def extract_all_ka_combinations(kao_combinations):
    sets, pairs, kes, remaining_tiles = kao_combinations
    all_ka_combinations = []

    kas = [(i, i+2) for i in range(1, 8)]  # 生成所有可能的卡张

    found_kas = False

    for ka in kas:
        ka_sets = []
        # 确保卡张的牌数量满足条件
        if all(ka.count(tile) <= remaining_tiles.count(tile) for tile in ka):
            ka_sets.append(list(ka))  # 提取卡张
            found_kas = True
            # 逐个减去每个组合中出现的数字
            for tile in ka:
                remaining_tiles.remove(tile)
            all_ka_combinations.append((sets.copy(), pairs.copy(), kes.copy(), ka_sets, remaining_tiles.copy()))

    if not found_kas:
        # 没有找到卡张，返回一个空白的卡张组合列表
        all_ka_combinations.append((sets.copy(), pairs.copy(), kes.copy(), [], remaining_tiles.copy()))

    return all_ka_combinations

def extract_single_tile_combinations(ka_combination):
    sets, pairs, kaos, kas, remaining_tiles = ka_combination
    all_single_tile_combinations = []

    single_tile_combinations = [[tile] for tile in remaining_tiles]

    all_single_tile_combinations.append((sets.copy(), pairs.copy(), kaos.copy(), kas.copy(), single_tile_combinations))

    return all_single_tile_combinations

def group_tiles(input_tiles):
    # 调用之前定义的函数获取所有组合
    triplet_combinations = extract_all_triplet_combinations(input_tiles)

    all_results = []

    # 遍历所有搭子组合
    for triplet_combination in triplet_combinations:
        pair_combinations = extract_all_pair_combinations(triplet_combination)
        for pair_combination in pair_combinations:
            kao_combinations = extract_all_kao_combinations(pair_combination)
            for kao_combination in kao_combinations:
                ka_combinations = extract_all_ka_combinations(kao_combination)
                for ka_combination in ka_combinations:
                    single_tile_combinations = extract_single_tile_combinations(ka_combination)
                    for single_tile_combination in single_tile_combinations:
                        all_results.append(single_tile_combination)

    return all_results

def modify_combinations(combination_list, suit_prefix):
    modified_combinations = []

    for sets, pairs, kaos, kas, single_tiles in combination_list:
        modified_sets = [[f"{suit_prefix}_{tile}" for tile in subset] for subset in sets]
        modified_pairs = [[f"{suit_prefix}_{tile}" for tile in pair] for pair in pairs]
        modified_kaos = [[f"{suit_prefix}_{tile}" for tile in kao] for kao in kaos]
        modified_kas = [[f"{suit_prefix}_{tile}" for tile in ka] for ka in kas]
        modified_single = [[f"{suit_prefix}_{tile}" for tile in subset] for subset in single_tiles]

        modified_combinations.append((modified_sets, modified_pairs, modified_kaos, modified_kas, modified_single))

    return modified_combinations

from itertools import product

def merge_combinations(bamboo_combinations=None, char_combinations=None, dot_combinations=None):
    merged_combinations = []
    
    # 对bamboo_combinations进行修改
    modified_bamboo_combinations = modify_combinations(bamboo_combinations, 'b')

    # 对char_combinations进行修改
    modified_char_combinations = modify_combinations(char_combinations, 'c')

    # 对dot_combinations进行修改
    modified_dot_combinations = modify_combinations(dot_combinations, 'd')

    # 获取每个花色的组合列表
    combinations_lists = [modified_bamboo_combinations, modified_char_combinations, modified_dot_combinations]

    # 生成每种花色的索引组合
    indices_combinations = list(product(*[range(len(lst)) if lst else [None] for lst in combinations_lists]))

    for indices_combination in indices_combinations:
        merged_combination = (
            sum([combinations_lists[i][j][0] for i, j in enumerate(indices_combination) if j is not None], []),
            sum([combinations_lists[i][j][1] for i, j in enumerate(indices_combination) if j is not None], []),
            sum([combinations_lists[i][j][2] for i, j in enumerate(indices_combination) if j is not None], []),
            sum([combinations_lists[i][j][3] for i, j in enumerate(indices_combination) if j is not None], []),
            sum([combinations_lists[i][j][4] for i, j in enumerate(indices_combination) if j is not None], [])
        )
        merged_combination = tuple(item for sublist in merged_combination for item in sublist)  # Flatten the tuple
        merged_combination = list(filter(None, merged_combination))  # Remove empty lists
        merged_combinations.append(merged_combination)

    return merged_combinations

def calculate_combination_stats(combination):
    stats = {
        'total_sets': len(combination),
        'triplet_count': 0,
        'pair_count': 0,
        'kao_count': 0,
        'ka_count': 0,
        'single_count': 0
    }

    for group in combination:
        # 判断是否为搭子
        is_triplet = len(group) == 3
        # 判断是否为对子
        is_pair = len(group) == 2 and all(tile[-1] == group[0][-1] for tile in group)
        # 判断是否为靠张
        is_kao = len(group) == 2 and int(group[0][-1]) +1 == int(group[1][-1])
        # 判断是否为卡张
        is_ka = len(group) == 2 and int(group[0][-1]) +2 == int(group[1][-1])
        # 判断是否为单牌
        is_single = len(group) == 1

        stats['triplet_count'] += is_triplet
        stats['pair_count'] += is_pair
        stats['kao_count'] += is_kao
        stats['ka_count'] += is_ka
        stats['single_count'] += is_single

    return stats

def extract_combinations(data_dict):
    extracted_list = []

    for combination, stats in data_dict.items():
        if stats['pair_count'] >= 5:
            extracted_list.append((combination, stats))

    min_total_sets = min(data_dict.values(), key=lambda x: x['total_sets'])['total_sets']

    min_total_sets_list = [(combination, stats) for combination, stats in data_dict.items() if stats['total_sets'] == min_total_sets]

    extracted_list.extend(min_total_sets_list)

    return extracted_list

def classify_set(s):
    
    # 判断是否为对子
    is_pair = len(s) == 2 and all(tile[-1] == s[0][-1] for tile in s)

    # 判断是否为靠张
    is_kao = len(s) == 2 and int(s[0][-1]) + 1 == int(s[1][-1])

    # 判断是否为卡张
    is_ka = len(s) == 2 and int(s[0][-1]) + 2 == int(s[1][-1])

    # 判断是否为单牌
    is_single = len(s) == 1

    # 返回分类结果
    if is_pair:
        return "pair"
    elif is_kao:
        return "kao"
    elif is_ka:
        return "ka"
    elif is_single:
        return "single"
    else:
        return "triple"

def classify_sets(combination):
    complete_sets = []
    incomplete_sets = []
    complete_set_counts = []

    # 检查对子数量
    pair_count = combination[1]['pair_count']
    
    # 另一些接下来要用到的stats
    triplet_count = combination[1]['triplet_count']
    kao_count = combination[1]['kao_count']
    ka_count = combination[1]['ka_count']

    if pair_count == 0:
        # 没有对子，只有搭子是完整牌组
        complete_sets = [s for s in combination[0] if classify_set(s) == "triple"]
        complete_set_counts = [len(complete_sets)]

        # 其他组是不完整牌组
        incomplete_sets = [s for s in combination[0] if classify_set(s) != "triple"]
        
    elif pair_count == 1:
        # 一个对子是完整牌组
        complete_sets = [s for s in combination[0] if classify_set(s) == "pair"]
        complete_sets.extend([s for s in combination[0] if classify_set(s) == "triple"])
        complete_set_counts = [len(complete_sets)]
        
        # 其他组是不完整牌组
        incomplete_sets = [s for s in combination[0] if classify_set(s) != "pair" and classify_set(s) != "triple"]
    
    elif pair_count > 1 and pair_count < 5:
        # 多个对子的情况，每个对子都可能是完整牌组
        complete_set = []
        incomplete_set = []
        pairs = [s for s in combination[0] if classify_set(s) == "pair"]
        counts = []
        for i in range(pair_count):
            complete_set = [pairs[i]]
            complete_set.extend([s for s in combination[0] if classify_set(s) == "triple"])
            incomplete_set = ([s for s in combination[0] if s != pairs[i] and classify_set(s) != "triple"])
            count = len(complete_set)
            counts.append(count)
            complete_sets.extend([complete_set])
            incomplete_sets.extend([incomplete_set])
        max_indices = [i for i, x in enumerate(counts) if x == max(counts)]
        for i in range(len(complete_sets)):
            if i not in max_indices:
                # 移除 complete_sets 中的第 i 个子列表
                del complete_sets[i]
                del incomplete_sets[i]
                del counts[i]
        complete_set_counts = counts

    elif pair_count >= 5:
        # 七对情况，所有对子都是完整牌组
        complete_sets = [s for s in combination[0] if classify_set(s) == "pair"]
        complete_set_counts = len(complete_sets)
        
        # 其他组是不完整牌组
        incomplete_sets = [s for s in combination[0] if classify_set(s) != "pair"]
    
    if not any(isinstance(item, list) for item in incomplete_sets):
        incomplete_sets = [incomplete_sets]
        
    if not any(isinstance(item, list) for item in complete_sets):
        complete_sets = [complete_sets]

    return complete_sets, incomplete_sets, pair_count, triplet_count, kao_count, ka_count

def update_incomplete_sets(incomplete, pair_count, triplet_count, kao_count, ka_count):
    
    # 打掉手牌后
    updated_sets = []

    for incomplete_set in incomplete:
        # 规则1：如果有单牌，打掉单牌
        single = [s for s in incomplete_set if classify_set(s) == "single"]
        if single:
            for discarded in single:
                updated_set = [s for s in incomplete_set if s != discarded]
                updated_sets.append({discarded[0]: updated_set})

        # 规则2：如果有特殊情况，打掉卡张或者靠张
        elif (
            pair_count == 2 or
            pair_count == 4 or
            pair_count == 5 or
            triplet_count + kao_count + ka_count == 6
        ):
            # 打掉所有卡张
            ka = [s for s in incomplete_set if classify_set(s) == "ka"]
            for index, i in enumerate(ka):
                ka_copy = list(ka[index])
                for discarded in ka_copy:
                    ka_remain = tuple([s for s in ka_copy if s != discarded])
                    updated_set = [s for s in incomplete_set if s != tuple(ka_copy)]
                    updated_set.append(ka_remain)
                    updated_sets.append({discarded: updated_set})

            # 如果没有卡张，打掉靠张
            if not ka:
                kao = [s for s in incomplete_set if classify_set(s) == "kao"]
                for index, i in enumerate(kao):
                    kao_copy = list(kao[index])
                    for discarded in kao_copy:
                        kao_remain = tuple([s for s in kao_copy if s != discarded])
                        updated_set = [s for s in incomplete_set if s != tuple(kao_copy)]
                        updated_set.append(kao_remain)
                        updated_sets.append({discarded: updated_set})

        # 规则3：如果有3个对子，打掉对子
        elif pair_count == 3:
            pair = [s for s in incomplete_set if classify_set(s) == "pair"]
            for index, i in enumerate(pair):
                pair_copy = list(pair[index])
                pair_remain = tuple([pair_copy[0]])
                updated_set = [s for s in incomplete_set if s != tuple(pair_copy)]
                updated_set.append(pair_remain)
                updated_sets.append({pair_remain: updated_set})
        
    updated_incomplete_sets = updated_sets

    return updated_incomplete_sets, pair_count

def find_possible_next_tiles(updated_incomplete_sets, pair_count):
    
    possible_next_tiles = []
    
    for updated_incomplete_set in updated_incomplete_sets:
        discard = tuple(list(updated_incomplete_set.keys())[0])
        if len(discard) > 1:
            discard = ''.join(discard)
        updated_incomplete_set = list(updated_incomplete_set.values())[0]
        possible = []

        for s in updated_incomplete_set:
            # 对子变成搭子
            if classify_set(s) == "pair":
                tile1, tile2 = s
                possible.append(tile1)

            # 靠张变成搭子
            elif classify_set(s) == "kao":
                tile1, tile2 = s
                if tile1[-1] != "1":
                    possible.append(tile1[0:2]+str(int(tile1[-1])-1))
                if tile2[-1] != "9":
                    possible.append(tile2[0:2]+str(int(tile2[-1])+1))

            # 卡张变搭子
            elif classify_set(s) == "ka":
                tile1, tile2 = s
                possible.append(tile1[0:2]+str(int(tile1[-1])+1))

            # 单牌变对子
            elif classify_set(s) == "single" and (pair_count == 0 or pair_count >= 5):
                tile = s[0]
                possible.append(tile)

        possible_next_tiles.append({discard: possible})

    return possible_next_tiles

def calculate_efficiency(combination, possible_next_tiles):
    efficiency = []
    
    for possible in possible_next_tiles:
        
        # 对于每个可能的下一张牌
        for tile in list(possible.values())[0]:
            total_efficiency = 0
            
            # 计算对应位置的 complete_set 中，该牌出现的次数
            occurrences = sum(1 for s in combination if tile in s)
            
            # 计算效果并累加到总效果
            efficiency_value = 4 - occurrences
            total_efficiency += efficiency_value
            
        efficiency.append({tuple(list(possible.keys())[0]):total_efficiency})
    
    keys = set(entry for item in efficiency for entry in item.keys())
    
    efficiency_result = []
    for key in keys:
        value = 0
        for i in efficiency:
            if list(i.keys())[0] == key:
                value += list(i.values())[0]
        if len(key) > 1:
            key = ''.join(key)
        efficiency_result.append({key:value})
    
    return efficiency_result

def find_best_move(efficiency_result):
    max_value = max(entry[list(entry.keys())[0]] for entry in efficiency_result)
    max_keys = [key for entry in efficiency_result for key, value in entry.items() if value == max_value]
    return max_keys

def consolidate_mahjong_code(hand_tiles):
    sorted_hand = sort_mahjong_tiles(hand_tiles)
    bamboo, char, dot = split_suit_and_convert_to_numeric(sorted_hand)

    bamboo_combinations = group_tiles(bamboo) if bamboo else []
    char_combinations = group_tiles(char) if char else []
    dot_combinations = group_tiles(dot) if dot else []

    merged_combinations = merge_combinations(bamboo_combinations, char_combinations, dot_combinations)

    result_dict = {tuple(tuple(item) if isinstance(item, list) else item for item in combination): calculate_combination_stats(combination) for combination in merged_combinations}

    extracted_combinations = extract_combinations(result_dict)
    
    efficiency = []

    best_move = []

    for combination in extracted_combinations:
        complete_sets, incomplete_sets, pair_count, triplet_count, kao_count, ka_count = classify_sets(combination)
        updated_incomplete_sets, pair_count = update_incomplete_sets(incomplete_sets, pair_count, triplet_count, kao_count, ka_count)
        possible_next_tiles = find_possible_next_tiles(updated_incomplete_sets, pair_count)
        efficiency_result = calculate_efficiency(combination, possible_next_tiles)
        efficiency.extend(efficiency_result)
    
    best_move = find_best_move(efficiency)
    best_move = list(set(best_move))
    
    return best_move