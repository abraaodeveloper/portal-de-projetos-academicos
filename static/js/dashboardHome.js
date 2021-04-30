var i = 0;
const acessos = document.getElementById('qtdAcess');
const usuarios = document.getElementById('qtdAccounts');
const projetosSoft = document.getElementById('qtdProjetcSoft');
const projetosBook = document.getElementById('qtdProjetcEbook');

function move() {

  if (i == 0) {
    i = 1;
    var elementoTwo = document.querySelector("#bar-two");
    var elementoOne = document.querySelector("#bar-one");
    var elementoThree = document.querySelector("#bar-three");
    var elementoFour = document.querySelector("#bar-four");
    var width = 0;
    var id = setInterval(frame, 80);

    function frame() {

      //acessos
      if (usuarios != null) {
        if (width >= acessos.value) {
          clearInterval(id);
          i = 0;
        }

        else {
          width++;
          elementoOne.style.width = width + " Acessos";
          elementoOne.innerHTML = width + " Acessos";
        }

        //usuários

        if (width >= usuarios.value) {
          clearInterval(id);
          i = 0;

        } else {
          width++;
          elementoTwo.style.width = width + " Contas";
          elementoTwo.innerHTML = width + " Contas";
        }


        //projetos de software
        if (width >= projetosSoft.value) {
          clearInterval(id);
          i = 0;

        } else {
          width++;
          elementoThree.style.width = width + " Projetos";
          elementoThree.innerHTML = width + " Projetos";
        }
        //Livros
        if (width >= projetosBook.value) {
          clearInterval(id);
          i = 0;

        } else {
          width++;
          elementoFour.style.width = width + " Livros";
          elementoFour.innerHTML = width + " Livros";
        }
      }
    }
  }
}

move();