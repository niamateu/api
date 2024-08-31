from django.shortcuts import render, get_object_or_404, redirect

from api.models import Food
from api.forms import FoodForm


# 一覧
def index(request):
    # foodモデル全てのレコードを取得してidの昇順に並べる
    foods = Food.objects.all().order_by('id')
    return render(request, 'foods/index.html',{'foods':foods})

# 新規、編集
def edit(request, id=None):
    # GETリクエストの処理
    if id:
        # 編集ボタンを押した場合
        food = get_object_or_404(Food,pk=id)
        # 編集画面フォームを生成
        form = FoodForm(instance=food)
    else:
        # 新規ボタンを押した場合
        food = Food()
        # 新規画面フォームを生成
        form = FoodForm(instance=food)

    # POSTリクエスト（保存）の処理
    if request.method == 'POST':
        # 追記されたフォームデータを渡す
        form = FoodForm(request.POST, instance=food)
        # フォームのバリデーション
        if form.is_valid():
            form.save()
            # 保存後、一覧ページにリダイレクト
            return redirect('api:index')

    # 新規・編集画面を表示
    return render(request, 'foods/edit.html', {'form':form,'id': id})

# 削除
def delete(request, id=None):
    # 指定されたidを元にデータベースから値を取得
    food = get_object_or_404(Food,pk=id)
    # 削除確認画面から送信されたリクエストは削除処理
    if request.method == 'POST':
        food.delete()
        return redirect('api:index')
    #　削除確認画面を表示
    return render(request, 'foods/delete.html', {'food':food,'id': id})

