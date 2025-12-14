import pytest
from src.customer import Customer
from src.loyalty_system import LoyaltySystem
from datetime import timedelta, datetime


# 1
def test_calcular_pontos_compra_cliente_padrao():
    system = LoyaltySystem()
    system.add_customer(Customer("Ana"))
    system.register_purchase("Ana", 10)
    assert system.get_points("Ana") == 10


# 2
def test_calcular_pontos_cliente_premium():
    system = LoyaltySystem()
    system.add_customer(Customer("Bob", "PREMIUM"))
    system.register_purchase("Bob", 10)
    assert system.get_points("Bob") == 15


# 3
def test_calcular_pontos_cliente_vip():
    system = LoyaltySystem()
    system.add_customer(Customer("Carlos", "VIP"))
    system.register_purchase("Carlos", 10)
    assert system.get_points("Carlos") == 20


# 4
def test_acumular_pontos_varias_compras():
    system = LoyaltySystem()
    system.add_customer(Customer("Ana"))
    system.register_purchase("Ana", 10)
    system.register_purchase("Ana", 20)
    assert system.get_points("Ana") == 30


# 5
def test_consultar_pontos_cliente_existente():
    system = LoyaltySystem()
    system.add_customer(Customer("Ana", points=50))
    assert system.get_points("Ana") == 50


# 6
def test_resgatar_pontos_para_desconto():
    system = LoyaltySystem()
    system.add_customer(Customer("Ana", points=100))
    desconto = system.redeem_points("Ana", 20)
    assert desconto == 1.0


# 7
def test_impedir_resgate_com_saldo_insuficiente():
    system = LoyaltySystem()
    system.add_customer(Customer("Ana", points=10))
    with pytest.raises(ValueError):
        system.redeem_points("Ana", 20)


# 8
def test_resgatar_todos_os_pontos_disponiveis():
    system = LoyaltySystem()
    system.add_customer(Customer("Ana", points=50))
    system.redeem_points("Ana", 50)
    assert system.get_points("Ana") == 0


# 9
def test_nao_gerar_pontos_para_valor_zero():
    system = LoyaltySystem()
    system.add_customer(Customer("Ana"))
    system.register_purchase("Ana", 0)
    assert system.get_points("Ana") == 0


# 10
def test_gerar_pontos_para_valores_decimais():
    system = LoyaltySystem()
    system.add_customer(Customer("Ana"))
    system.register_purchase("Ana", 10.5)
    assert system.get_points("Ana") == 10.5


# 11
def test_nao_permitir_pontos_negativos():
    system = LoyaltySystem()
    system.add_customer(Customer("Ana", points=10))
    system.redeem_points("Ana", 10)
    assert system.get_points("Ana") == 0


# 12
def test_cliente_inexistente_lanca_excecao():
    system = LoyaltySystem()
    with pytest.raises(ValueError):
        system.get_points("Ghost")


# 13
def test_registrar_novo_cliente_com_pontos_iniciais():
    customer = Customer("Ana", points=30)
    assert customer.points == 30


# 14
def test_aplicar_bonus_promocional_em_compra():
    system = LoyaltySystem()
    system.add_customer(Customer("Ana"))
    system.register_purchase("Ana", 10, bonus=5)
    assert system.get_points("Ana") == 15


# 15
def test_expirar_pontos_antigos_apos_periodo():
    system = LoyaltySystem()
    customer = Customer("Ana")
    customer.history.append({"points": 20, "date": datetime.now() - timedelta(days=40)})
    customer.points = 20
    system.add_customer(customer)
    system.expire_old_points(30)
    assert system.get_points("Ana") == 0


# 16
def test_registrar_varios_clientes_em_lista():
    system = LoyaltySystem()
    system.add_customer(Customer("A"))
    system.add_customer(Customer("B"))
    assert len(system.customers) == 2


# 17
def test_calcular_pontos_lista_clientes():
    system = LoyaltySystem()
    system.add_customer(Customer("A", points=10))
    system.add_customer(Customer("B", points=20))
    assert system.total_points() == 30


# 18
def test_filtrar_clientes_com_pontos_acima_de_limite():
    system = LoyaltySystem()
    system.add_customer(Customer("A", points=10))
    system.add_customer(Customer("B", points=50))
    result = system.filter_customers_above_points(20)
    assert len(result) == 1


# 19
def test_ordenar_clientes_por_pontos():
    system = LoyaltySystem()
    system.add_customer(Customer("A", points=10))
    system.add_customer(Customer("B", points=50))
    ordered = system.sort_customers_by_points()
    assert ordered[0].name == "B"


# 20
def test_remover_clientes_com_saldo_zero():
    system = LoyaltySystem()
    system.add_customer(Customer("A", points=0))
    system.add_customer(Customer("B", points=10))
    system.remove_customers_with_zero_points()
    assert len(system.customers) == 1


# 21
def test_buscar_cliente_por_nome():
    system = LoyaltySystem()
    system.add_customer(Customer("Ana"))
    customer = system.find_customer("Ana")
    assert customer.name == "Ana"


# 22
def test_somar_total_pontos_lista():
    system = LoyaltySystem()
    system.add_customer(Customer("A", points=10))
    system.add_customer(Customer("B", points=20))
    assert system.total_points() == 30


# 23
def test_ranking_clientes_por_pontos():
    system = LoyaltySystem()
    system.add_customer(Customer("A", points=10))
    system.add_customer(Customer("B", points=30))
    system.add_customer(Customer("C", points=20))
    ranking = system.sort_customers_by_points()
    assert [c.name for c in ranking] == ["B", "C", "A"]


# 24
def test_manter_pontos_validos_apos_expiracao():
    system = LoyaltySystem()
    customer = Customer("Ana")

    customer.history = [
        {"points": 20, "date": datetime.now() - timedelta(days=40)},  # expira
        {"points": 30, "date": datetime.now() - timedelta(days=10)},  # válido
    ]
    customer.points = 50

    system.add_customer(customer)

    system.expire_old_points(30)

    # Apenas os pontos válidos permanecem
    assert system.get_points("Ana") == 30


# 25
def test_criar_cliente_sem_nome_lanca_excecao():
    with pytest.raises(ValueError):
        Customer("")
