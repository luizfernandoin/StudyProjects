function setLocalStorage(itens) {
    localStorage.setItem("listaDeCompras", JSON.stringify(itens));
}

function getLocalStorage() {
    const data = localStorage.getItem('listaDeCompras');
    if (data) {
        listaDeCompras.itens = JSON.parse(data);
    }
}

const listaDeCompras = {
    itens: [],

    adicionar(item) {
        this.itens.push(item);
        setLocalStorage(this.itens);
    },
    remover(item) {
        const index = this.itens.findIndex(element => element.codigoBarra === item.codigoBarra);
        if (index >= 0) {
            this.itens.splice(index, 1);
            setLocalStorage(this.itens);
        }
    },
    marcar(item) {
        const index = this.itens.findIndex(element => element.codigoBarra === item.codigoBarra);
        if (index >= 0) {
            this.itens[index].comprado = true;
            setLocalStorage(this.itens);
        }
    },
    desmarcar(item) {
        const index = this.itens.findIndex(element => element.codigoBarra === item.codigoBarra);
        if (index >= 0) {
            this.itens[index].comprado = false;
            setLocalStorage(this.itens);
        }
    },
    listar() {
        return this.itens;
    }
}

getLocalStorage();

export default listaDeCompras;
