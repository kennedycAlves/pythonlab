
[root@localhost Volweb01]# cat acesso/cadastro.html
<HTML>
        <HEAD>
                <TITLE>Formulario de cadastro</TITLE>
        </HEAD>
  <BODY>
<FORM  method="POST" action="cadastrar.php?acao=adicionar">
<TR>
<TD>Nome Completo:</TD>
<TD><INPUT type="text" name="FormNome" maxlength=32></TD>
</TR>
<BR>
<TR>
<TD>Sexo:</TD>
<TD><INPUT type="radio" value="Masculino" name="FormSexo" maxlength=10></TD>
Masculino
<INPUT type="radio" value="Feminino" name="FormSexo" maxlength=10>
Feminino
</TD>
</TR>
<BR>
<TR>
<TD>E-Mail:</TD>
<TD><INPUT type"text" name="FormEmail" maxlength=64></TD>
</TR>
<BR>
<TR>
<TD>DDD:</TD>
<TD><INPUT type="text" name="FormDDD" maxlength=4></TD>
<TD>Telefone:</TD>
<TD><INPUT type="text" name="FormTelefone" maxlength=10></TD>
</TR>
<BR>
<TR>
<TD>Cidade:</TD>
<TD><INPUT name="FormCidade" maxlength=28></TD>
</TR>
<BR>
<TR>
<TD>Estado:</TD>
<TD><SELECT name="FormEstado">
        <option> Selecione...</option>
        <option value="AC">AC</option>
        <option value="AL">AL</option>
        <option value="AP">AP</option>
        <option value="AM">AM</option>
        <option value="BA">BA</option>
        <option value="CE">CE</option>
        <option value="ES">ES</option>
        <option value="DF">DF</option>
        <option value="MA">MA</option>
        <option value="MT">MT</option>
        <option value="MS">MS</option>
        <option value="MG">MG</option>
        <option value="PA">PA</option>
        <option value="PB">PB</option>
        <option value="PR">PR</option>
        <option value="PE">PE</option>
        <option value="PI">PI</option>
        <option value="RJ">RJ</option>
        <option value="RN">RN</option>
        <option value="RS">RS</option>
        <option value="RO">RO</option>
        <option value="RR">RR</option>
        <option value="SC">SC</option>
        <option value="SP">SP</option>
        <option value="SE">SE</option>
        <option value="TO">TO</option>
   </TD> </SELECT>
</TR>
<BR>
<TR>
<TD>Login:</TD>
<TD><INPUT type="text" name="FormLogin"></TD>
<TD>Senha:</TD>
<TD><INPUT type="password" name="FormSenha"></TD>
<BR>
<INPUT type="submit" name="cadastrar" value="Cadastrar">
<INPUT type="reset" name"limpar" value="Limpar">
[root@localhost Volweb01]#




[root@localhost Volweb01]# cat acesso/cadastrar.php
<?php

## Conectar no banco

$servidor = 'mysql_DB_01';
$login = 'root';
$senha = 'pass';
$banco = "USUARIO";

$link = mysqli_connect($servidor, $login, $senha, $banco)
        or die("Nao foi possivel conectar no banco" . mysqli_error());

##Conectando na base da dos

$select = mysqli_select_db($link, $banco);

if($_REQUEST["acao"] == "adicionar")
{

$nome = $_POST["FormNome"];
$cidade = $_POST["FormCidade"];
$email = $_POST["FormEmail"];
$telefone = $_POST["FormTelefone"];
$sexo = $_POST["FormSexo"];
$ddd = $_POST["FormDDD"];
$login = $_POST["FormLogin"];
$senha = $_POST["FormSenha"];
$crypt = crypt($senha);
$estado = $_POST["FormEstado"];

##Criando INSET do dados

$sql = "INSERT INTO CADASTRO (CIDADE, DDD, EMAIL, ESTADO, LOGIN, NOME, SENHA, SEXO, TELEFONE) VALUES('$cidade', '$ddd', '$email', '$estado', '$login', '$nome', '$crypt', '$sexo', '$telefone')";

##Executar instrucao SQL

$executa = mysqli_query($link,$sql);

if(!$executa)
{
die('Erro: ' . mysqli_error());
}

else
{
echo "Operacao realizada com sucesso!";
}
}



?>
<BR>
<A href="http://10.61.217.181:8282/acesso/cadastro.html">Voltar</A>
[root@localhost Volweb01]#


