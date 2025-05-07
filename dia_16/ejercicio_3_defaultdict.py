from collections import defaultdict

def sistema_votacion():
    candidatos = {'fabio','ana','pedro'}
    votos = defaultdict(dict)

    try:
        print("Candidatos disponibles:", candidatos)
        for i in range(5):  
            voto = input(f"Voto {i+1}/5 (o 'salir' para finalizar): ")
            if voto.lower() == 'salir':
                break
            if not voto.strip():
                raise ValueError("El voto no puede estar vacío.")
            if voto not in candidatos:
                raise ValueError(f"El candidato '{voto}' no está en la lista.")
                    
            votos[voto] += 1

        print("\nResultados de la votación:")
        for candidato in candidatos:
            print(f"{candidato}: {votos[candidato]} votos")
        return True
    except ValueError as e:
        print(f"Error: {e}")
        return True
    except KeyboardInterrupt:
        print("El sistema fue interrumpido por el usuario.")
        return False
    
def main():
    while True:
        if not sistema_votacion():
            break
        print("\nVolvamos a intentar.")

if __name__ == '__main__':
    main()


