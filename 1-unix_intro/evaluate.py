import os, sys, glob
import pandas as pd

def main(results_dir, target_folder):
	print("results_dir", results_dir)
	print("target_folder", target_folder)
	target_path = os.path.join(results_dir, target_folder)
	results_csv_path = os.path.join(results_dir, "marks.csv")
	# json_files = glob.glob(jsons_dir, recursive=False)
	students_folds = glob.glob(f"{results_dir}/*/", recursive=False)
	students_folds.remove(target_path+"/")
	# print(students_folds)
	target_dict = get_excercises_dict(target_path)
	for student_fold in students_folds:
		student_dict = get_excercises_dict(student_fold)
		print("student_fold", student_fold)
		print("student_dict", student_dict)
		evaluate_student(student_dict, target_dict)
		save_results(student_dict, results_csv_path)


def save_results(student_dict, results_csv_path):
	headers = list(student_dict.keys())
	values_list = list(student_dict.values())
	values = [value["score"] for value in values_list]
	headers = ["name"] + headers
	values  = [values_list[0]["name"]] + values
	writeLineToCSV(results_csv_path, headers, values)


def evaluate_student(student_dict, target_dict):
	for key, value in target_dict.items():
		if not key in list(student_dict.keys()):
			student_dict[key] = {
				"name":list(student_dict.values())[0]["name"],
				"title":value["title"],
				"path":"",
				"score":0,
			}
		else:
			exc_path = student_dict[key]["path"]
			tar_path = value["path"]
			with open(exc_path) as f: 
				exc = f.readlines()
				exc = "".join([line.strip() for line in exc])
			with open(tar_path) as f: 
				tar = f.readlines()
				tar = "".join([line.strip() for line in tar])
			score = 1 if exc == tar else 0
			student_dict[key]["score"] = score

def get_excercises_dict(target_path):
	txt_files = glob.glob(target_path+"/*.txt", recursive=False)
	excercises = {}
	for txt_file in txt_files:
		txt_basename = os.path.basename(txt_file).replace(".txt", "")
		txt_items = txt_basename.split("_")
		txt_user = txt_items[0]
		txt_exc  = txt_items[1] + "_" + txt_items[2] + "_" + txt_items[3]
		excercise = {
			"title": txt_exc,
			"name": txt_user,
			"path": txt_file,
		}
		excercises[txt_exc] = excercise
	return excercises

def writeLineToCSV(csvPath, headers, values):
    '''Write one line to CSV
    example : writeLineToCSV("test.csv", ["a", "b", "c"], ["something",16,34])
    '''
    LastSlashPos = csvPath.rfind(os.path.split(csvPath)[-1]) - 1
    if not os.path.exists(csvPath[:LastSlashPos]): os.makedirs(csvPath[:LastSlashPos])
    dic = {}
    for i, header in enumerate(headers): dic[header] = values[i]
    data = [dic]
    if os.path.exists(csvPath): 
        df = pd.read_csv(csvPath)
        if values[0] in list(df[headers[0]]):
        	df.loc['name':values[0]] = values
        else:
        	df = df.append(data, ignore_index=True, sort=False)
    else:
        df = pd.DataFrame(data, columns = headers)
    df.to_csv(csvPath, index=False)

if __name__ == '__main__':
	results_dir = sys.argv[1]
	target_folder = sys.argv[2]
	main(results_dir, target_folder)