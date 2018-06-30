#!/usr/bin/env python
# -*- coding: utf-8 -*-

# statuses: 状態集合
# output: 出力結果（列）
# transitionP: 状態遷移確率
# outputP: 各状態ごとにそれぞれの出力がどれくらいの確率で生じるか
# initialP: 初期の状態の確率
	# initialP = {"S1": 0.2, "S2": 0.8}

import copy

def estimate_status(statuses, output, transitionP, outputP, initialP):
	counter = 0
	# 必要変数の初期化
	currentVi = {}
	for s in statuses:
			viData = {"probability": initialP[s], "path": []}
			currentVi[s] = viData
	for o in output:
		counter+=1
		pastVi = copy.deepcopy(currentVi)
		# print("*************************************\n")
		# print(str(counter)+"回目のoutput"+str(o)+"を検証します。\n")
		# print("現在のpastViは\n")
		# print (pastVi.items())
		# print("\n")
		# print("***********\n")
		for s in statuses:
			max_p = 0
			max_p_path = "error"
			for s_past in statuses:
				new_p = pastVi[s_past]["probability"]*transitionP[s_past][s]
				if new_p > max_p:
					max_p = new_p
					max_p_path = copy.deepcopy(pastVi[s_past]["path"])
					max_p_path.append(s)
			currentVi[s]["probability"] = max_p*outputP[s][o]
			currentVi[s]["path"] = max_p_path
			# print ("状態「"+s+"」では、")
	# 最後どちらが大きいかを決定して、resultを算出する
	result_p = 0
	for s in statuses:
		cv = currentVi[s]
		if cv["probability"] > result_p:
			result_p = cv["probability"]
			result_path = cv["path"]
	# 最後に結果を表示させる
	for rp in result_path:
		print (rp+"→")
	print ("\n 確率："+str(result_p))

	# pastVi = initialP
	# for o in output:





################################################################################
################################################################################

statuses = ["TrueDICE", "FalseDICE"]
output = [6, 6, 3, 6, 5, 6, 6, 1, 5, 4, 2, 3, 6, 1, 5, 2]
transitionP = {"TrueDICE": {"TrueDICE": 0.95, "FalseDICE": 0.05}, 
				"FalseDICE": {"TrueDICE": 0.1, "FalseDICE": 0.9}}
outputP = {"TrueDICE": {1: 0.167, 2: 0.167, 3: 0.167, 4: 0.167, 5: 0.167, 6: 0.167}, 
				"FalseDICE": {1: 0.01, 2: 0.01, 3: 0.01, 4: 0.01, 5: 0.01, 6: 0.5}}
initialP = {"TrueDICE": 0, "FalseDICE": 1}

estimate_status(statuses, output, transitionP, outputP, initialP)
