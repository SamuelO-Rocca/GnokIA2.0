import os
import json
from mcp.Provider_Tecnology.techinical_bases import base_tecnica

class Tecnology:
    def __init__(self, path_memory_tecnology = "project/src/mcp/memory/memory_tecnology.json"):
        self.base = base_tecnica() if callable(base_tecnica) else base_tecnica
        self.path_memory_tecnology = path_memory_tecnology
        os.makedirs(os.path.dirname(self.path_memory_tecnology), exist_ok=True)
        self.memory = self.upload_memory_Tecnology()
    
    def upload_memory_Tecnology(self):
        try:
            with open(self.path_memory_tecnology, 'r', encoding= "utf-8") as upload_memory:
                return json.load(upload_memory)
        except FileNotFoundError:
            return {}
        
    def save_memory_Tecnology(self, key=None, value=None):
        if key and value:
            self.memory[key] = value
        with open(self.path_memory_tecnology, 'w', encoding= "utf-8") as save_memory:
            json.dump(self.memory, save_memory, ensure_ascii=False, indent=4)

    def consult_memory_Tecnology(self,key):
        key = key.lower()
        result = {}

        for category, items in self.base["Linguagens_de_Programacao"].items():
            if key in category.lower():
                result[category] = items
            elif key in items["descricao"].lower():
                    result[category] = items
            else:
                for campo in items.values():
                    if isinstance(campo, list) and any(key in item.lower() for item in campo):
                        result[category] = items
                        break

        return result
    
    def category_list_Tecnology(self):
        return list(self.base["Linguagens_de_Programacao"].keys())
    
    def update_base_Tecnology(self, name, datas):
        self.base["Linguagens_de_Programacao"][name] = datas
        if "new_knwoledge" not in self.memory:
            self.memory["new_knwoledge"] = []
        self.memory["new_knwoledge"].append({name: datas})
        self.save_memory_Tecnology()
        return f"Update base has been updated with {name} and saved to memory."

    def generate_response_Tecnology(self, key):
        key = key.lower().strip()

        words = key.split()
        for word in words:
            if word in self.base['Linguagens_de_Programacao']:
                key = word
                break

        result = self.consult_memory_Tecnology(key)
        if not result:
            return{'message': f"No information found for '{key}'."}
        
        if len(result) == 1:
            linguagem, detalhes = next(iter(result.items()))
            response = f"Linguagem: {linguagem}\nDescrição: {detalhes['descricao']}\n Uso comum: {', '.join(detalhes['usos_comuns'])}\nFerramentas: {', '.join(detalhes['ferramentas'])}\n"
            return response
        else:
            return result
        
    def Save_Tecnology_Tecnology(self, name, datas):
        result = self.update_base_Tecnology(name, datas)
        