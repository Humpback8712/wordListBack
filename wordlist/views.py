from django.views import View
from .models import Wordlist4, Wordlist6, RankScoreList
from django.http import JsonResponse
import json
import random


class Words4View(View):

    def get(self, request):
        # 查询所有单词对象
        words = Wordlist4.objects.all()
        word_list = []
        for word in words:
             word_list.append({
                 'id': word.id,
                 'word': word.word
             })
        random.shuffle(word_list)
        return JsonResponse(word_list, safe=False)


class Words6View(View):

    def get(self, request):
        # 查询所有单词对象
        words = Wordlist6.objects.all()
        word_list = []
        for word in words:
             word_list.append({
                 'id': word.id,
                 'word': word.word
             })
        random.shuffle(word_list)
        return JsonResponse(word_list, safe=False)


class RankView(View):

    def get(self, request):
        ranks = RankScoreList.objects.all()
        ranks_list = []
        for obj in ranks:
            ranks_list.append({
                'score': obj.score,
                'name': obj.name
            })
        ranks_list.sort(key=lambda x: x["score"])
        ranks_list.reverse()
        rank_list = ranks_list[0:10]
        return JsonResponse(rank_list, safe=False)

    def post(self, request):
        # 前端发送json数据 在请求体中
        data = request.body.decode()
        data_dict = json.loads(data)
        uname = data_dict.get('uname')
        score = data_dict.get('score')
        Rank = RankScoreList.objects.create(score=score, name=uname)
        if uname is None:
            return JsonResponse({'error': '错误信息'}, status=400)
        else:
            return JsonResponse({'success': '成功'}, status=200)
    # 获取前端数据
    # 验证数据
    # 保存数据
    # 返回结果
    pass


