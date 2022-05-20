import time

# ===========================================
# 文字列内の重複チェック
def check_unique_chars(check_str):
    # 文字が128byte以上の場合：false
    if len(check_str) > 128:
        return False

    # 空の128byteのリストを作成(ASCIIを想定)
    check_list = [None] * 128

    # 引数の文字列を1文字ずつ取り出して比較
    for i in range(0, len(check_str)):
        val = check_str[i]      # 引数の文字列から1文字ずつ取得

        # リスト内に重複が存在する場合：false
        if val in check_list:
            return False

        check_list[i] = val     # リストに文字を格納
    return True

# print用の自作関数作成
def custom_print(arg_name, arg):
    print(f'{arg_name}：{arg}')
# ===========================================

# 実施処理
start_time = time.time()

if __name__ == '__main__':
    custom_print('__name__', __name__)
    check_str = 'abcdefgabcdefg'

custom_print('文字の長さ', len(check_str))
custom_print('判定結果', check_unique_chars(check_str))
custom_print('処理実行時間', time.time() - start_time)