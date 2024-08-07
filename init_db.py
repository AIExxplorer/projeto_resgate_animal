from app import create_app, db
from app.models import Animal, Doacao, Doador
from datetime import datetime

app = create_app()

def init_db():
    with app.app_context():
        # Cria todas as tabelas
        db.create_all()
        
        # Verifica se já existem dados no banco
        if Animal.query.first() is None:
            # Adiciona alguns dados de exemplo
            cachorro = Animal(nome='Rex', especie='Cachorro', raca='Labrador', data_resgate=datetime(2023, 6, 1))
            gato = Animal(nome='Whiskers', especie='Gato', raca='Siamês', data_resgate=datetime(2023, 6, 2))
            
            doador1 = Doador(nome='João Silva', email='joao@example.com')
            doador2 = Doador(nome='Maria Souza', email='maria@example.com')
            
            doacao1 = Doacao(valor=100.00, data=datetime(2023, 6, 3), doador=doador1)
            doacao2 = Doacao(valor=50.00, data=datetime(2023, 6, 4), doador=doador2)
            
            db.session.add_all([cachorro, gato, doador1, doador2, doacao1, doacao2])
            db.session.commit()
            
            print("Dados de exemplo adicionados com sucesso!")
        else:
            print("O banco de dados já contém dados. Nenhum dado de exemplo foi adicionado.")

if __name__ == '__main__':
    init_db()
    print("Banco de dados inicializado com sucesso!")