# -*- coding: utf-8 -*-
model = numpy.load("lstm_model.npz")
tparams = lstm.init_tparams(model)

(use_noise, x, mask, y, f_pred_prob, f_pred, cost) = lstm.build_model(tparams, 
                                                                      'encoder': 'lstm',
                                                                      'dim_proj': 128,
                                                                      'use_dropout': True,
)

# 最低限に簡略化
def pred_probs(f_pred_prob, sentence):
    probs = numpy.zeros((1, 2)).astype(config.floatX)
    x, mask, _y = imdb.prepare_data([sentence],
                                    1, # dummy。利用されないので適当に。
                                    maxlen=None)
    return f_pred_prob(x, mask)[0]

# それぞれ文字列を数値化した入力
sentences = [
    {
        "data": [27, 72, 104, 150, 19, 8, 106, 23],
        "text": "とても良い会社だ"
    },
    {
        "data": [27, 72, 104, 402, 121, 73, 8, 106, 23],
        "text": "とても最悪な会社だ"
    }
]

for sentence in sentences:
    result = pred_probs(f_pred_prob, sentence["data"])
    print "==="
    print result
    print sentence["text"], ("is positive" if (result[0] < result[1]) else "is negative")
