from rest_framework import permissions


class CreateBet(permissions.BasePermission):
	message = "Desculpe, Contas administradoras ou Gerentes não são apropriados para criarem apostas. Use contas normais ou conta de vendedor."

	def has_permission(self, request, view):		
		if request.method in permissions.SAFE_METHODS:			
			if not request.GET.get('store'):				
				self.message = "Forneça a id da loja"
				return False
			return True
		else:			
			if not request.GET.get('store'):
				self.message = "Forneça a id da loja"
				return False
			elif request.user.is_superuser or request.user.has_perm("user.be_manager"):			
				return False			
			elif request.user.has_perm('user.be_seller') and str(request.user.seller.my_store.id) != str(request.GET['store']):
				self.message = "Usuario não é pertencente a esta banca"
				return False
			elif request.user.has_perm('user.be_punter') and str(request.user.punter.my_store.id) != str(request.GET['store']):				
				self.message = "Usuario não é pertencente a esta banca"				
				return False			
			return True


class PayWinnerPermission(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.user.has_perm('user.be_seller'):
			if not str(request.GET['store']):
				self.message = "Entrada da banca não inserida"				
				return False
			if str(request.user.seller.my_store.id) != str(request.GET['store']):
				self.message = "Ticket não é pertencente a esta banca"
				return False
		self.message = "Usuário não é vendedor"
		return True